
"""
Telegram Downloader v3.4 (UI 2026-ready) - PyQt6
- File Type Filters (Photos, Videos, etc.)
- Sequential Download Queue (Auto-start next)
- Language Selector (Hebrew/English)
- Expanded About Dialog
- Improved Multi-selection (Shift + Click)
- Individual Download Progress Tracking
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Literal, Any, Dict

from PyQt6.QtCore import (
    Qt, QSettings, QThread, pyqtSignal, QSize, QSortFilterProxyModel, QModelIndex, QAbstractTableModel
)
from PyQt6.QtGui import QAction, QFont, QIcon, QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QSpinBox, QComboBox, QMessageBox, QStackedWidget, QFrame, QFileDialog,
    QTableView, QHeaderView, QAbstractItemView, QProgressBar, QTextEdit, QCheckBox, QInputDialog,
    QStyle, QStyleOptionButton, QToolBar, QMenu
)

# --- i18n support ---
from i18n import Translation

# --- Optional deps ---
try:
    from telethon import TelegramClient
    from telethon.errors import SessionPasswordNeededError
    from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
    TELETHON_AVAILABLE = True
except Exception:
    TELETHON_AVAILABLE = False

try:
    import humanize
    HUMANIZE_AVAILABLE = True
except Exception:
    HUMANIZE_AVAILABLE = False


APP_ORG = "TelegramDownloader"
APP_NAME = "TelegramDownloader"
APP_VERSION = "3.4"


# ----------------------------
# Logging
# ----------------------------
def _setup_logging(log_dir: Path) -> Path:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "app.log"
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    for h in list(logger.handlers): logger.removeHandler(h)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    sh.setLevel(logging.INFO)
    logger.addHandler(sh)
    logging.info("=== Telegram Downloader v%s started ===", APP_VERSION)
    return log_path


def _format_size(num_bytes: Optional[int]) -> str:
    if num_bytes is None: return "—"
    try:
        if HUMANIZE_AVAILABLE: return humanize.naturalsize(num_bytes, binary=True)
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if num_bytes < 1024.0: return f"{num_bytes:,.1f} {unit}"
            num_bytes /= 1024.0
        return f"{num_bytes:,.1f} PB"
    except Exception: return str(num_bytes)


MediaKind = Literal["photo", "image", "video", "document", "archive", "file"]


@dataclass
class MediaItem:
    chat_ref: str
    msg_id: int
    date_iso: str
    name: str
    size: Optional[int]
    kind: MediaKind
    selected: bool = False

    @property
    def date_dt(self) -> datetime:
        try: return datetime.fromisoformat(self.date_iso)
        except Exception: return datetime.min


# ----------------------------
# Thread workers
# ----------------------------
class AuthThread(QThread):
    code_needed = pyqtSignal(str)
    password_needed = pyqtSignal()
    success = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, api_id: int, api_hash: str, session_path: Path, phone: str):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.phone = api_id, api_hash, session_path, phone
        self.code, self.password = None, None

    def run(self) -> None:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self._auth(client))
            loop.close()
        except Exception as e:
            logging.exception("Auth thread failed")
            self.error.emit(str(e))

    async def _auth(self, client: TelegramClient) -> None:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(self.phone)
            self.code_needed.emit(self.phone)
            while self.code is None: await asyncio.sleep(0.1)
            try:
                await client.sign_in(self.phone, self.code)
            except SessionPasswordNeededError:
                self.password_needed.emit()
                while self.password is None: await asyncio.sleep(0.1)
                await client.sign_in(password=self.password)
        await client.disconnect()
        self.success.emit()


class ScanThread(QThread):
    progress = pyqtSignal(int, str)
    result = pyqtSignal(list)
    error = pyqtSignal(str)

    def __init__(self, api_id: int, api_hash: str, session_path: Path, chat_ref: str, limit: int):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.chat_ref, self.limit = api_id, api_hash, session_path, chat_ref, limit
        self._stop = False

    def stop(self) -> None: self._stop = True

    def run(self) -> None:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self._scan(client))
            loop.close()
        except Exception as e:
            logging.exception("Scan thread failed")
            self.error.emit(str(e))

    async def _scan(self, client: TelegramClient) -> None:
        try:
            await client.connect()
            if not await client.is_user_authorized(): raise RuntimeError("Not authorized")
            self.progress.emit(10, "Connecting...")
            entity = await client.get_entity(self.chat_ref)
            messages = await client.get_messages(entity, limit=self.limit)
            items: List[MediaItem] = []
            total = max(1, len(messages))
            for i, msg in enumerate(messages, start=1):
                if self._stop: break
                if not msg or not msg.media: continue
                name, size, kind = f"msg_{msg.id}", None, "file"
                if isinstance(msg.media, MessageMediaPhoto):
                    kind, name = "photo", f"photo_{msg.id}.jpg"
                elif isinstance(msg.media, MessageMediaDocument):
                    doc = msg.media.document
                    size = getattr(doc, "size", None)
                    filename = None
                    for attr in getattr(doc, "attributes", []):
                        fn = getattr(attr, "file_name", None)
                        if fn: filename = fn; break
                    if not filename: filename = f"file_{msg.id}"
                    name = filename
                    low = filename.lower()
                    if low.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")): kind = "image"
                    elif low.endswith((".mp4", ".avi", ".mkv", ".mov", ".webm")): kind = "video"
                    elif low.endswith((".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt")): kind = "document"
                    elif low.endswith((".zip", ".rar", ".7z", ".tar", ".gz")): kind = "archive"
                    else: kind = "file"
                items.append(MediaItem(chat_ref=self.chat_ref, msg_id=int(msg.id), date_iso=(msg.date.isoformat() if msg.date else ""), name=str(name), size=size, kind=kind))
                if i % 25 == 0: self.progress.emit(min(95, 60 + int(35 * (i / total))), f"Analyzed {i}/{total}...")
            self.progress.emit(100, f"Found {len(items)} items")
            self.result.emit(items)
        finally:
            try: await client.disconnect()
            except: pass


class DownloadThread(QThread):
    # pct, name, done, total, cur_done, cur_total
    progress = pyqtSignal(int, str, int, int, int, int)
    finished = pyqtSignal(int, int, str)
    error = pyqtSignal(str)

    def __init__(self, api_id: int, api_hash: str, session_path: Path, items: List[MediaItem], out_dir: Path):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.items, self.out_dir = api_id, api_hash, session_path, items, out_dir
        self._stop = False

    def stop(self) -> None: self._stop = True

    def run(self) -> None:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self._download(client))
            loop.close()
        except Exception as e:
            logging.exception("Download thread failed")
            self.error.emit(str(e))

    async def _download(self, client: TelegramClient) -> None:
        try:
            await client.connect()
            if not await client.is_user_authorized(): raise RuntimeError("Not authorized")
            self.out_dir.mkdir(parents=True, exist_ok=True)
            ok, fail, total = 0, 0, len(self.items)
            for i, item in enumerate(self.items, start=1):
                if self._stop: break
                try:
                    entity = await client.get_entity(item.chat_ref)
                    msg = await client.get_messages(entity, ids=item.msg_id)
                    if not msg or not msg.media: fail += 1; continue
                    safe_name = "".join(c for c in item.name if c.isalnum() or c in "._- ")
                    dest = self.out_dir / safe_name
                    def _prog_callback(received, total_bytes):
                        if total_bytes: self.progress.emit(int(100 * (received / total_bytes)), item.name, i, total, received, total_bytes)
                    await client.download_media(msg, file=str(dest), progress_callback=_prog_callback)
                    ok += 1
                except Exception: fail += 1
                self.progress.emit(100, item.name, i, total, item.size or 0, item.size or 0)
            self.finished.emit(ok, fail, str(self.out_dir))
        finally:
            try: await client.disconnect()
            except: pass


# ----------------------------
# Table Model
# ----------------------------
class MediaTableModel(QAbstractTableModel):
    def __init__(self, data: List[MediaItem]):
        super().__init__()
        self._raw_data = data
        self.headers = ["V", "ID", "תאריך", "שם קובץ", "גודל", "סוג"]

    def rowCount(self, parent=QModelIndex()) -> int: return len(self._raw_data)
    def columnCount(self, parent=QModelIndex()) -> int: return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid(): return None
        row, col = index.row(), index.column()
        item = self._raw_data[row]
        if role == Qt.ItemDataRole.DisplayRole:
            if col == 1: return item.msg_id
            if col == 2: return item.date_iso.split("T")[0]
            if col == 3: return item.name
            if col == 4: return _format_size(item.size)
            if col == 5: return item.kind
        if role == Qt.ItemDataRole.CheckStateRole and col == 0:
            return Qt.CheckState.Checked if item.selected else Qt.CheckState.Unchecked
        if role == Qt.ItemDataRole.TextAlignmentRole: return Qt.AlignmentFlag.AlignCenter
        if role == Qt.ItemDataRole.ForegroundRole: return QColor("#000000")
        return None

    def setData(self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if index.isValid() and role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            self._raw_data[index.row()].selected = (value == Qt.CheckState.Checked)
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.CheckStateRole])
            return True
        return False

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid(): return Qt.ItemFlag.NoItemFlags
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        return base | Qt.ItemFlag.ItemIsUserCheckable if index.column() == 0 else base

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole: return self.headers[section]
        return None


# ----------------------------
# Main Window
# ----------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Telegram Downloader v{APP_VERSION}")
        self.resize(1150, 800)
        self.base_dir = Path.home() / ".telegram_downloader"
        self.log_path = _setup_logging(self.base_dir)
        self.session_path = self.base_dir / "user.session"
        self.settings = QSettings(APP_ORG, APP_NAME)
        self.lang_code = self.settings.value("language", "he")
        self.i18n = Translation(self.lang_code)
        self.all_items: List[MediaItem] = []
        self.scan_thread, self.dl_thread, self.auth_thread = None, None, None
        self._build_ui()
        self._load_settings()
        self._refresh_auth_state()
        self._apply_language()

    def _build_ui(self):
        tb = self.addToolBar("main")
        tb.setMovable(False)
        tb.setIconSize(QSize(20, 20))
        tb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["עברית", "English"])
        self.lang_combo.setCurrentIndex(0 if self.lang_code == "he" else 1)
        self.lang_combo.currentIndexChanged.connect(self._change_language)
        tb.addWidget(QLabel("  שפה / Language: "))
        tb.addWidget(self.lang_combo)
        tb.addSeparator()
        self.act_open_logs = QAction("פתח לוג", self)
        self.act_open_logs.triggered.connect(self.open_log_file)
        tb.addAction(self.act_open_logs)
        self.act_about = QAction("אודות", self)
        self.act_about.triggered.connect(self.show_about)
        tb.addAction(self.act_about)
        tb.addSeparator()
        self.act_exit = QAction("יציאה", self)
        self.act_exit.triggered.connect(self.close)
        tb.addAction(self.act_exit)

        root = QWidget()
        self.setCentralWidget(root)
        root_l = QHBoxLayout(root)
        root_l.setContentsMargins(0, 0, 0, 0)
        root_l.setSpacing(0)

        nav = QFrame()
        nav.setObjectName("nav")
        nav.setFixedWidth(240)
        nav_l = QVBoxLayout(nav)
        nav_l.setContentsMargins(16, 16, 16, 16)
        nav_l.setSpacing(10)
        self.title_label = QLabel("📥 Telegram\nDownloader")
        self.title_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.title_label.setObjectName("brand")
        nav_l.addWidget(self.title_label)
        self.btn_setup = QPushButton("1) הגדרות")
        self.btn_scan = QPushButton("2) סריקה")
        self.btn_library = QPushButton("3) בחירה")
        self.btn_download = QPushButton("4) הורדה")
        for b in [self.btn_setup, self.btn_scan, self.btn_library, self.btn_download]:
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(42)
            b.setObjectName("navBtn")
            nav_l.addWidget(b)
        nav_l.addStretch()
        self.auth_badge = QLabel("סטטוס: לא מחובר")
        self.auth_badge.setObjectName("badgeBad")
        nav_l.addWidget(self.auth_badge)
        self.btn_exit_side = QPushButton("יציאה מסודרת")
        self.btn_exit_side.setObjectName("danger")
        self.btn_exit_side.setFixedHeight(45)
        self.btn_exit_side.clicked.connect(self.close)
        nav_l.addWidget(self.btn_exit_side)
        root_l.addWidget(nav)

        self.stack = QStackedWidget()
        root_l.addWidget(self.stack, 1)
        self.page_setup = self._page_setup()
        self.page_scan = self._page_scan()
        self.page_library = self._page_library()
        self.page_download = self._page_download()
        self.stack.addWidget(self.page_setup)
        self.stack.addWidget(self.page_scan)
        self.stack.addWidget(self.page_library)
        self.stack.addWidget(self.page_download)
        self.btn_setup.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_setup))
        self.btn_scan.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_scan))
        self.btn_library.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_library))
        self.btn_download.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_download))
        self._apply_styles()

    def _apply_styles(self):
        self.setStyleSheet("""
        QMainWindow, QWidget { background-color: #ffffff; color: #000000; }
        QLabel { color: #000000; font-size: 14px; }
        QFrame#nav { background-color: #f8f9fa; border-left: 2px solid #dee2e6; border-right: 2px solid #dee2e6; }
        QLabel#brand { color: #0056b3; margin-bottom: 15px; font-size: 22px; }
        QToolBar { background-color: #f8f9fa; border-bottom: 1px solid #dee2e6; padding: 5px; }
        QPushButton#navBtn { text-align: center; padding: 10px 15px; border: 1px solid #ced4da; border-radius: 6px; background-color: #ffffff; color: #212529; font-weight: bold; }
        QPushButton#navBtn:hover { background-color: #e9ecef; border-color: #adb5bd; color: #0056b3; }
        QLabel#badgeBad { padding: 10px; border-radius: 6px; background-color: #f8d7da; border: 2px solid #f5c6cb; color: #721c24; font-weight: bold; }
        QLabel#badgeOk { padding: 10px; border-radius: 6px; background-color: #d4edda; border: 2px solid #c3e6cb; color: #155724; font-weight: bold; }
        QLineEdit, QSpinBox, QComboBox, QTextEdit { background-color: #ffffff; border: 2px solid #ced4da; border-radius: 6px; padding: 8px 12px; color: #000000; }
        QPushButton { border-radius: 6px; padding: 10px 20px; border: 2px solid #ced4da; background-color: #f8f9fa; color: #212529; font-weight: bold; }
        QPushButton#primary { background-color: #007bff; border: 2px solid #0069d9; color: #ffffff; }
        QPushButton#danger { background-color: #dc3545; border: 2px solid #c82333; color: #ffffff; }
        QProgressBar { border: 2px solid #ced4da; border-radius: 6px; text-align: center; background-color: #e9ecef; height: 25px; color: #000000; font-weight: bold; }
        QProgressBar::chunk { background-color: #28a745; border-radius: 4px; }
        QTableView { background-color: #ffffff; gridline-color: #dee2e6; border: 2px solid #ced4da; border-radius: 6px; selection-background-color: #e7f1ff; selection-color: #000000; color: #000000; }
        QHeaderView::section { background-color: #f1f3f5; border: 1px solid #dee2e6; padding: 12px; color: #212529; font-weight: bold; }
        """)

    def _page_setup(self) -> QWidget:
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(40, 40, 40, 40); l.setSpacing(20)
        self.setup_title = QLabel("הגדרות וחיבור לטלגרם"); self.setup_title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold)); l.addWidget(self.setup_title)
        grid = QVBoxLayout()
        self.in_api_id = QLineEdit(); self.label_api_id = QLabel("API ID:"); grid.addWidget(self.label_api_id); grid.addWidget(self.in_api_id)
        self.in_api_hash = QLineEdit(); self.label_api_hash = QLabel("API HASH:"); grid.addWidget(self.label_api_hash); grid.addWidget(self.in_api_hash)
        self.in_phone = QLineEdit(); self.label_phone = QLabel("מספר טלפון:"); grid.addWidget(self.label_phone); grid.addWidget(self.in_phone)
        l.addLayout(grid)
        self.chk_autologin = QCheckBox("התחבר אוטומטית בהפעלה"); self.chk_autologin.setChecked(True); l.addWidget(self.chk_autologin)
        row = QHBoxLayout(); self.btn_save = QPushButton("שמור והתחבר"); self.btn_save.setObjectName("primary"); self.btn_save.clicked.connect(self.save_and_auth); row.addWidget(self.btn_save)
        self.btn_clear = QPushButton("איפוס הגדרות"); self.btn_clear.setObjectName("danger"); self.btn_clear.clicked.connect(self.clear_settings); row.addWidget(self.btn_clear); row.addStretch(); l.addLayout(row)
        self.auth_box = QTextEdit(); self.auth_box.setReadOnly(True); self.auth_box.setFixedHeight(180); l.addWidget(self.auth_box); l.addStretch(); return w

    def _page_scan(self) -> QWidget:
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(40, 40, 40, 40); l.setSpacing(20)
        self.scan_title = QLabel("סריקת קבוצה / ערוץ"); self.scan_title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold)); l.addWidget(self.scan_title)
        self.in_chat = QLineEdit(); self.label_chat = QLabel("קישור או שם המשתמש:"); l.addWidget(self.label_chat); l.addWidget(self.in_chat)
        row = QHBoxLayout(); self.spin_limit = QSpinBox(); self.spin_limit.setRange(10, 100000); self.spin_limit.setValue(1000); self.label_limit = QLabel("כמות הודעות:"); row.addWidget(self.label_limit); row.addWidget(self.spin_limit); row.addStretch(); l.addLayout(row)
        self.scan_status = QLabel("סטטוס: מוכן"); l.addWidget(self.scan_status)
        self.scan_progress = QProgressBar(); self.scan_progress.setVisible(False); l.addWidget(self.scan_progress)
        self.btn_start_scan = QPushButton("התחל סריקה"); self.btn_start_scan.setObjectName("primary"); self.btn_start_scan.clicked.connect(self.start_scan); l.addWidget(self.btn_start_scan); l.addStretch(); return w

    def _page_library(self) -> QWidget:
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(20, 20, 20, 20); l.setSpacing(15)
        top = QHBoxLayout(); self.lib_title = QLabel("תוצאות סריקה"); self.lib_title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold)); top.addWidget(self.lib_title); top.addStretch(); self.lib_count = QLabel("0 פריטים"); top.addWidget(self.lib_count); l.addLayout(top)
        f_row = QHBoxLayout()
        self.in_filter = QLineEdit(); self.in_filter.setPlaceholderText("חיפוש..."); self.in_filter.textChanged.connect(self._apply_filter); f_row.addWidget(self.in_filter)
        self.combo_kind = QComboBox(); self.combo_kind.addItems(["הכל", "photo", "video", "document", "archive"]); self.combo_kind.currentTextChanged.connect(self._apply_filter); f_row.addWidget(self.combo_kind)
        l.addLayout(f_row)
        self.table = QTableView(); self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); self.table.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection); self.table.setSortingEnabled(True); self.table.horizontalHeader().setStretchLastSection(True); l.addWidget(self.table)
        self.table.clicked.connect(self._on_table_clicked)
        bot = QHBoxLayout(); self.btn_sel_all = QPushButton("בחר הכל"); self.btn_sel_all.clicked.connect(self._select_all); bot.addWidget(self.btn_sel_all)
        self.btn_sel_none = QPushButton("בטל בחירה"); self.btn_sel_none.clicked.connect(self._select_none); bot.addWidget(self.btn_sel_none); bot.addStretch()
        self.btn_go_dl = QPushButton("המשך להורדה (0)"); self.btn_go_dl.setObjectName("primary"); self.btn_go_dl.clicked.connect(self.prepare_download); bot.addWidget(self.btn_go_dl); l.addLayout(bot); return w

    def _page_download(self) -> QWidget:
        w = QWidget(); l = QVBoxLayout(w); l.setContentsMargins(40, 40, 40, 40); l.setSpacing(20)
        self.dl_title = QLabel("תהליך הורדה"); self.dl_title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold)); l.addWidget(self.dl_title)
        self.dl_info = QLabel("ממתין..."); l.addWidget(self.dl_info)
        self.label_total_prog = QLabel("התקדמות כללית:"); l.addWidget(self.label_total_prog); self.dl_progress_total = QProgressBar(); l.addWidget(self.dl_progress_total)
        self.dl_current_label = QLabel("קובץ נוכחי: -"); l.addWidget(self.dl_current_label); self.dl_progress_item = QProgressBar(); l.addWidget(self.dl_progress_item)
        self.dl_log = QTextEdit(); self.dl_log.setReadOnly(True); l.addWidget(self.dl_log)
        row = QHBoxLayout(); self.btn_start_dl = QPushButton("התחל הורדה"); self.btn_start_dl.setObjectName("primary"); self.btn_start_dl.clicked.connect(self.start_download); row.addWidget(self.btn_start_dl)
        self.btn_stop_dl = QPushButton("עצור"); self.btn_stop_dl.setObjectName("danger"); self.btn_stop_dl.clicked.connect(self.stop_download); row.addWidget(self.btn_stop_dl); row.addStretch(); l.addLayout(row); return w

    def _change_language(self, index):
        new_lang = "he" if index == 0 else "en"
        if new_lang != self.lang_code:
            self.lang_code = new_lang; self.settings.setValue("language", new_lang); self.i18n.set_language(new_lang); self._apply_language()

    def _apply_language(self):
        is_rtl = (self.lang_code == "he"); self.setLayoutDirection(Qt.LayoutDirection.RightToLeft if is_rtl else Qt.LayoutDirection.LeftToRight)
        self.act_open_logs.setText("פתח לוג" if is_rtl else "Open Logs"); self.act_about.setText(self.i18n.get("menu_about")); self.act_exit.setText("יציאה" if is_rtl else "Exit")
        self.btn_setup.setText(self.i18n.get("step_setup")); self.btn_scan.setText(self.i18n.get("step_scan")); self.btn_library.setText(self.i18n.get("step_select")); self.btn_download.setText(self.i18n.get("step_download")); self.btn_exit_side.setText("יציאה מסודרת" if is_rtl else "Exit App")
        self.setup_title.setText(self.i18n.get("setup_title")); self.label_api_id.setText(self.i18n.get("label_api_id")); self.label_api_hash.setText(self.i18n.get("label_api_hash")); self.label_phone.setText(self.i18n.get("label_phone")); self.btn_save.setText(self.i18n.get("btn_save_continue"))
        self.scan_title.setText(self.i18n.get("scan_title")); self.label_chat.setText(self.i18n.get("scan_group_label")); self.label_limit.setText(self.i18n.get("scan_max_messages")); self.btn_start_scan.setText(self.i18n.get("btn_start_scan"))
        self.lib_title.setText(self.i18n.get("select_title")); self.btn_sel_all.setText(self.i18n.get("btn_select_all")); self.btn_sel_none.setText(self.i18n.get("btn_select_none"))
        self.dl_title.setText(self.i18n.get("step_download")); self.btn_start_dl.setText(self.i18n.get("btn_download_selected")); self.btn_stop_dl.setText(self.i18n.get("btn_stop_download"))

    def _on_table_clicked(self, index: QModelIndex):
        rows = self.table.selectionModel().selectedRows()
        for item in self.all_items: item.selected = False
        for idx in rows: self.all_items[idx.row()].selected = True
        self.table.viewport().update(); self._update_sel_count()

    def _select_all(self):
        for item in self.all_items: item.selected = True
        self.table.selectAll(); self.table.viewport().update(); self._update_sel_count()

    def _select_none(self):
        for item in self.all_items: item.selected = False
        self.table.clearSelection(); self.table.viewport().update(); self._update_sel_count()

    def _update_sel_count(self):
        count = sum(1 for item in self.all_items if item.selected)
        self.btn_go_dl.setText(f"{self.i18n.get('step_download')} ({count})")

    def _load_settings(self):
        self.in_api_id.setText(self.settings.value("api_id", "")); self.in_api_hash.setText(self.settings.value("api_hash", "")); self.in_phone.setText(self.settings.value("phone", "")); self.chk_autologin.setChecked(self.settings.value("autologin", "true") == "true")
        if self.chk_autologin.isChecked() and self.in_api_id.text(): self.save_and_auth()

    def _refresh_auth_state(self):
        if self.session_path.exists(): self.auth_badge.setText("סטטוס: מחובר"); self.auth_badge.setObjectName("badgeOk")
        else: self.auth_badge.setText("סטטוס: לא מחובר"); self.auth_badge.setObjectName("badgeBad")
        self.auth_badge.setStyle(self.auth_badge.style())

    def save_and_auth(self):
        api_id, api_hash, phone = self.in_api_id.text().strip(), self.in_api_hash.text().strip(), self.in_phone.text().strip()
        if not (api_id and api_hash and phone): return
        self.settings.setValue("api_id", api_id); self.settings.setValue("api_hash", api_hash); self.settings.setValue("phone", phone)
        self.auth_thread = AuthThread(int(api_id), api_hash, self.session_path, phone)
        self.auth_thread.code_needed.connect(self._on_code_needed); self.auth_thread.password_needed.connect(self._on_pass_needed); self.auth_thread.success.connect(self._on_auth_success); self.auth_thread.error.connect(self._on_auth_error); self.auth_thread.start()

    def _on_code_needed(self, phone):
        code, ok = QInputDialog.getText(self, self.i18n.get("dialog_code_title"), f"{self.i18n.get('dialog_code_message', phone=phone)}")
        if ok: self.auth_thread.code = code

    def _on_pass_needed(self):
        pwd, ok = QInputDialog.getText(self, self.i18n.get("dialog_password_title"), self.i18n.get("dialog_password_message"), QLineEdit.EchoMode.Password)
        if ok: self.auth_thread.password = pwd

    def _on_auth_success(self): self.auth_box.append("✅ מחובר!"); self._refresh_auth_state()
    def _on_auth_error(self, err): self.auth_box.append(f"❌ שגיאה: {err}")
    def clear_settings(self):
        self.settings.clear()
        if self.session_path.exists():
            self.session_path.unlink()
        self._refresh_auth_state()

    def start_scan(self):
        chat = self.in_chat.text().strip()
        if not chat: return
        self.scan_progress.setVisible(True); self.scan_thread = ScanThread(int(self.settings.value("api_id")), self.settings.value("api_hash"), self.session_path, chat, self.spin_limit.value())
        self.scan_thread.progress.connect(self._on_scan_progress); self.scan_thread.result.connect(self._on_scan_result); self.scan_thread.start()

    def _on_scan_progress(self, pct, msg): self.scan_progress.setValue(pct); self.scan_status.setText(msg)
    def _on_scan_result(self, items): self.all_items = items; self.lib_count.setText(f"{len(items)} פריטים"); model = MediaTableModel(items); self.table.setModel(model); self.table.resizeColumnsToContents(); self.stack.setCurrentWidget(self.page_library)

    def _apply_filter(self):
        txt, kind = self.in_filter.text().lower(), self.combo_kind.currentText()
        filtered = [it for it in self.all_items if txt in it.name.lower() and (kind == "הכל" or it.kind == kind)]
        model = MediaTableModel(filtered); self.table.setModel(model)

    def prepare_download(self):
        selected = [it for it in self.all_items if it.selected]
        if not selected: return
        self.stack.setCurrentWidget(self.page_download); self.dl_info.setText(f"מוכן להורדת {len(selected)} קבצים.")

    def start_download(self):
        selected = [it for it in self.all_items if it.selected]
        out_dir = QFileDialog.getExistingDirectory(self, "בחר תיקייה")
        if not out_dir: return
        self.dl_thread = DownloadThread(int(self.settings.value("api_id")), self.settings.value("api_hash"), self.session_path, selected, Path(out_dir))
        self.dl_thread.progress.connect(self._on_dl_progress); self.dl_thread.finished.connect(self._on_dl_finished); self.dl_thread.start()

    def stop_download(self):
        if self.dl_thread: self.dl_thread.stop()

    def _on_dl_progress(self, pct, name, done, total, cur_done, cur_total):
        self.dl_progress_total.setValue(int(((done - 1) / total) * 100 + (pct / total)))
        self.dl_current_label.setText(f"מוריד: {name} ({_format_size(cur_done)} / {_format_size(cur_total)})"); self.dl_progress_item.setValue(pct)
        if pct == 100: self.dl_log.append(f"✅ הושלם: {name}")

    def _on_dl_finished(self, ok, fail, folder): QMessageBox.information(self, "סיום", f"הורדו {ok} קבצים ל-{folder}")
    def open_log_file(self): os.startfile(self.log_path) if sys.platform == "win32" else None
    def show_about(self):
        about = f"<h2>Telegram Downloader v{APP_VERSION}</h2><p><b>נוצר על ידי: Aviel.AI</b></p><p>כלי מקצועי להורדת מדיה מטלגרם.</p><br><p><b>תכונות:</b></p><ul><li>מסנני סוג קובץ (תמונות, וידאו וכו')</li><li>תור הורדה טורי אוטומטי</li><li>תמיכה מלאה בעברית ואנגלית</li><li>בחירה מרובה חכמה (Shift+Click)</li></ul>"
        QMessageBox.about(self, self.i18n.get("about_title"), about)

if __name__ == "__main__":
    app = QApplication(sys.argv); app.setStyle("Fusion"); window = MainWindow(); window.show(); sys.exit(app.exec())
