"""
Telegram Desktop Downloader v2.2.0 ULTIMATE PRO
מוריד טלגרם - גרסת ULTIMATE PRO המתקדמת ביותר
Created by Aviel.AI
"""

import sys
import asyncio
import os
import time
import subprocess
from pathlib import Path
from typing import Optional, List, Dict
import webbrowser
from datetime import datetime
import humanize

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QSettings, QSize, QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QImage

from i18n import tr, get_translator

try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
    from telethon.errors import SessionPasswordNeededError
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# --- ULTIMATE PRO STYLESHEETS ---
LIGHT_STYLE = """
QMainWindow { background-color: #f8f9fa; }
QWidget { font-family: 'Segoe UI', 'Arial', sans-serif; }
QPushButton { border-radius: 8px; padding: 10px 20px; font-weight: bold; }
QPushButton#primaryBtn { background-color: #0088cc; color: white; border: none; }
QPushButton#successBtn { background-color: #28a745; color: white; border: none; }
QPushButton#dangerBtn { background-color: #dc3545; color: white; border: none; }
QLineEdit, QSpinBox, QComboBox { border: 2px solid #dee2e6; border-radius: 6px; padding: 8px; background-color: white; }
QGroupBox { font-weight: bold; border: 1px solid #dee2e6; border-radius: 8px; margin-top: 15px; padding-top: 15px; }
QProgressBar { border: 1px solid #dee2e6; border-radius: 10px; text-align: center; height: 20px; }
QProgressBar::chunk { background-color: #0088cc; border-radius: 9px; }
"""

DARK_STYLE = """
QMainWindow { background-color: #121212; color: #e0e0e0; }
QWidget { font-family: 'Segoe UI', 'Arial', sans-serif; color: #e0e0e0; }
QPushButton { border-radius: 8px; padding: 10px 20px; font-weight: bold; }
QPushButton#primaryBtn { background-color: #0088cc; color: white; border: none; }
QPushButton#successBtn { background-color: #2e7d32; color: white; border: none; }
QPushButton#dangerBtn { background-color: #c62828; color: white; border: none; }
QLineEdit, QSpinBox, QComboBox { border: 2px solid #333; border-radius: 6px; padding: 8px; background-color: #1e1e1e; color: white; }
QGroupBox { font-weight: bold; border: 1px solid #333; border-radius: 8px; margin-top: 15px; padding-top: 15px; color: #0088cc; }
QProgressBar { border: 1px solid #333; border-radius: 10px; text-align: center; height: 20px; background-color: #1e1e1e; }
QProgressBar::chunk { background-color: #0088cc; border-radius: 9px; }
QScrollArea { border: none; background-color: transparent; }
QFrame#mediaItem { background-color: #1e1e1e; border: 1px solid #333; }
QLabel { color: #e0e0e0; }
"""

class AuthThread(QThread):
    code_needed = pyqtSignal(str)
    password_needed = pyqtSignal()
    auth_success = pyqtSignal()
    auth_error = pyqtSignal(str)
    
    def __init__(self, api_id, api_hash, session_path, phone):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.phone = api_id, api_hash, session_path, phone
        self.code = self.password = None
    
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self.authenticate(client))
            loop.close()
        except Exception as e: self.auth_error.emit(str(e))
    
    async def authenticate(self, client):
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(self.phone)
            self.code_needed.emit(self.phone)
            while self.code is None: await asyncio.sleep(0.1)
            try: await client.sign_in(self.phone, self.code)
            except SessionPasswordNeededError:
                self.password_needed.emit()
                while self.password is None: await asyncio.sleep(0.1)
                await client.sign_in(password=self.password)
        await client.disconnect()
        self.auth_success.emit()

class ScanThread(QThread):
    progress = pyqtSignal(int, str)
    content_found = pyqtSignal(list)
    error = pyqtSignal(str)
    
    def __init__(self, api_id, api_hash, session_path, group_link, max_messages):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.group_link, self.max_messages = api_id, api_hash, session_path, group_link, max_messages
        self.is_running = True
    
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self.scan_content(client))
            loop.close()
        except Exception as e: self.error.emit(str(e))
    
    async def scan_content(self, client):
        try:
            await client.connect()
            self.progress.emit(10, tr("scan_connecting"))
            entity = await client.get_entity(self.group_link)
            self.progress.emit(30, tr("scan_scanning"))
            messages = await client.get_messages(entity, limit=self.max_messages)
            self.progress.emit(50, tr("scan_analyzing"))
            media_items = []
            for msg in messages:
                if not self.is_running: break
                if msg.media:
                    item = {'id': msg.id, 'date': msg.date, 'message': msg, 'type': 'file', 'name': f"file_{msg.id}", 'size': 0, 'thumb': None}
                    if isinstance(msg.media, MessageMediaPhoto):
                        item['type'] = 'photo'
                        item['name'] = f"photo_{msg.id}.jpg"
                    elif isinstance(msg.media, MessageMediaDocument):
                        doc = msg.media.document
                        item['size'] = doc.size
                        filename = next((attr.file_name for attr in doc.attributes if hasattr(attr, 'file_name')), f"file_{msg.id}")
                        item['name'] = filename
                        ext = filename.lower()
                        if ext.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')): item['type'] = 'image'
                        elif ext.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')): item['type'] = 'video'
                        elif ext.endswith(('.pdf', '.doc', '.docx', '.txt', '.epub')): item['type'] = 'document'
                        elif ext.endswith(('.zip', '.rar', '.7z', '.tar', '.gz')): item['type'] = 'archive'
                        else: item['type'] = 'file'
                    media_items.append(item)
            self.progress.emit(100, tr("scan_found_files", count=len(media_items)))
            self.content_found.emit(media_items)
            await client.disconnect()
        except Exception as e: self.error.emit(str(e))
    
    def stop(self): self.is_running = False

class ParallelDownloadThread(QThread):
    """ULTIMATE Parallel Downloader with Speed and ETA"""
    progress = pyqtSignal(int, str, int, int, str, str) # p, name, current, total, speed, eta
    finished = pyqtSignal(int, int)
    
    def __init__(self, api_id, api_hash, session_path, items, download_path, concurrent=3):
        super().__init__()
        self.api_id, self.api_hash, self.session_path, self.items, self.download_path = api_id, api_hash, session_path, items, Path(download_path)
        self.concurrent = concurrent
        self.is_running = True
        self.downloaded = 0
        self.failed = 0
        self.start_time = 0
        self.total_bytes = 0
    
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(str(self.session_path), self.api_id, self.api_hash, loop=loop)
            loop.run_until_complete(self.start_parallel(client))
            loop.close()
        except Exception: self.finished.emit(self.downloaded, self.failed)

    async def start_parallel(self, client):
        await client.connect()
        self.start_time = time.time()
        semaphore = asyncio.Semaphore(self.concurrent)
        tasks = []
        for i, item in enumerate(self.items):
            tasks.append(self.download_item(client, item, i, semaphore))
        await asyncio.gather(*tasks)
        await client.disconnect()
        self.finished.emit(self.downloaded, self.failed)

    async def download_item(self, client, item, index, semaphore):
        async with semaphore:
            if not self.is_running: return
            try:
                file_path = self.download_path / item['name']
                # Resume Support
                if file_path.exists() and file_path.stat().st_size == item['size'] and item['size'] > 0:
                    self.downloaded += 1
                    self.update_stats(item['name'], index + 1)
                    return

                def prog_callback(received, total):
                    if not self.is_running: raise Exception("Stopped")
                    self.total_bytes += received
                    self.update_stats(item['name'], index + 1)

                await client.download_media(item['message'], file=str(file_path), progress_callback=prog_callback)
                self.downloaded += 1
            except Exception: self.failed += 1

    def update_stats(self, name, current):
        elapsed = time.time() - self.start_time
        speed_val = self.total_bytes / elapsed if elapsed > 0 else 0
        speed_str = f"{humanize.naturalsize(speed_val)}/s"
        
        # ETA calculation
        remaining_items = len(self.items) - self.downloaded
        if self.downloaded > 0:
            avg_time = elapsed / self.downloaded
            eta_val = avg_time * remaining_items
            eta_str = str(datetime.utcfromtimestamp(eta_val).strftime('%H:%M:%S'))
        else: eta_str = "--:--:--"
        
        p = int((current / len(self.items)) * 100)
        self.progress.emit(p, name, current, len(self.items), speed_str, eta_str)

    def stop(self): self.is_running = False

class MediaItemWidget(QFrame):
    changed = pyqtSignal()
    def __init__(self, item: dict, is_dark=False):
        super().__init__()
        self.item = item
        self.is_dark = is_dark
        self.init_ui()
    
    def init_ui(self):
        self.setObjectName("mediaItem")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        bg = "#1e1e1e" if self.is_dark else "white"
        border = "#333" if self.is_dark else "#e9ecef"
        hover = "#2d2d2d" if self.is_dark else "#f1f3f5"
        
        self.setStyleSheet(f"QFrame#mediaItem {{ background-color: {bg}; border: 1px solid {border}; border-radius: 10px; }} QFrame#mediaItem:hover {{ background-color: {hover}; border-color: #0088cc; }}")
        
        layout = QHBoxLayout(self)
        self.checkbox = QCheckBox(); self.checkbox.setChecked(True); self.checkbox.stateChanged.connect(lambda: self.changed.emit()); layout.addWidget(self.checkbox)
        
        icon_map = {'photo': '📷', 'image': '🖼️', 'video': '🎬', 'document': '📄', 'archive': '📦', 'file': '📎'}
        self.icon_lab = QLabel(icon_map.get(self.item['type'], '📎')); self.icon_lab.setFont(QFont("Arial", 16)); layout.addWidget(self.icon_lab)
        
        info_l = QVBoxLayout(); name_lab = QLabel(self.item['name']); name_lab.setStyleSheet(f"font-weight: bold; color: {'#fff' if self.is_dark else '#343a40'};"); info_l.addWidget(name_lab)
        meta_l = QHBoxLayout(); size_lab = QLabel(humanize.naturalsize(self.item['size'])); size_lab.setStyleSheet("color: #6c757d; font-size: 11px;"); meta_l.addWidget(size_lab)
        date_lab = QLabel(self.item['date'].strftime("%d/%m/%Y")); date_lab.setStyleSheet("color: #888; font-size: 11px;"); meta_l.addWidget(date_lab); meta_l.addStretch(); info_l.addLayout(meta_l)
        layout.addLayout(info_l, 1)

    def is_checked(self): return self.checkbox.isChecked()
    def set_checked(self, c): self.checkbox.setChecked(c)

class ModernWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings('AvielAI', 'TelegramDownloaderUltimate')
        self.translator = get_translator()
        self.is_dark = self.settings.value('theme', 'light') == 'dark'
        self.translator.set_language(self.settings.value('language', 'he'))
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet(DARK_STYLE if self.is_dark else LIGHT_STYLE)
        self.setWindowTitle(f"{tr('app_name')} {tr('app_version')}")
        self.resize(1100, 850)
        
        central = QWidget(); self.setCentralWidget(central)
        self.main_l = QVBoxLayout(central); self.main_l.setContentsMargins(0, 0, 0, 0); self.main_l.setSpacing(0)
        
        header = QFrame(); header.setFixedHeight(70); header.setStyleSheet(f"background-color: {'#1e1e1e' if self.is_dark else 'white'}; border-bottom: 1px solid {'#333' if self.is_dark else '#dee2e6'};")
        h_l = QHBoxLayout(header); h_l.addWidget(QLabel(f"⚡ {tr('app_name')} <span style='color: #0088cc;'>ULTIMATE</span>", font=QFont("Arial", 18, QFont.Weight.Bold))); h_l.addStretch()
        
        self.theme_btn = QPushButton("🌙" if not self.is_dark else "☀️"); self.theme_btn.setFixedSize(40, 40); self.theme_btn.clicked.connect(self.toggle_theme); h_l.addWidget(self.theme_btn)
        self.menu_btn = QPushButton("⚙️"); self.menu_btn.setFixedSize(40, 40); self.menu_btn.clicked.connect(self.show_settings_menu); h_l.addWidget(self.menu_btn)
        self.main_l.addWidget(header)
        
        self.steps_w = self.create_steps_indicator(); self.main_l.addWidget(self.steps_w)
        self.stack = QStackedWidget(); self.main_l.addWidget(self.stack)
        
        self.stack.addWidget(self.create_setup_page())
        self.stack.addWidget(self.create_scan_page())
        self.stack.addWidget(self.create_select_page())
        self.stack.addWidget(self.create_download_page())
        
        if self.settings.value('api_id'): self.init_telegram_client(); self.show_scan_page()
        else: self.show_setup_page()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.settings.setValue('theme', 'dark' if self.is_dark else 'light')
        self.init_ui()

    def show_settings_menu(self):
        menu = QMenu(self); lang_m = menu.addMenu(tr("menu_language"))
        for c, n in self.translator.get_available_languages().items():
            a = lang_m.addAction(n); a.triggered.connect(lambda checked, code=c: self.change_lang(code))
        menu.addSeparator(); menu.addAction("Logout", self.logout); menu.addAction(tr("menu_about"), self.show_about)
        menu.exec(self.menu_btn.mapToGlobal(self.menu_btn.rect().bottomLeft()))

    def change_lang(self, c): self.settings.setValue('language', c); self.translator.set_language(c); self.init_ui()

    def create_steps_indicator(self):
        w = QFrame(); w.setFixedHeight(80); w.setStyleSheet(f"background-color: {'#121212' if self.is_dark else '#f8f9fa'}; border-bottom: 1px solid {'#333' if self.is_dark else '#dee2e6'};")
        l = QHBoxLayout(w); l.setContentsMargins(100, 0, 100, 0)
        self.step_widgets = []
        for i, name in enumerate([tr("step_setup"), tr("step_scan"), tr("step_select"), tr("step_download")]):
            sw = QWidget(); sl = QVBoxLayout(sw); c = QLabel(str(i+1)); c.setFixedSize(30, 30); c.setAlignment(Qt.AlignmentFlag.AlignCenter); c.setStyleSheet("background: #dee2e6; border-radius: 15px; color: white; font-weight: bold;")
            sl.addWidget(c, 0, Qt.AlignmentFlag.AlignCenter); lab = QLabel(name); lab.setFont(QFont("Arial", 9)); lab.setStyleSheet("color: #6c757d;"); sl.addWidget(lab, 0, Qt.AlignmentFlag.AlignCenter)
            self.step_widgets.append((c, lab)); l.addWidget(sw)
            if i < 3: line = QFrame(); line.setFrameShape(QFrame.Shape.HLine); line.setStyleSheet("color: #dee2e6;"); l.addWidget(line, 1)
        return w

    def update_progress_step(self, step: int):
        for i, (c, l) in enumerate(self.step_widgets):
            active = i + 1 <= step
            c.setStyleSheet(f"background: {'#0088cc' if active else '#dee2e6'}; border-radius: 15px; color: white; font-weight: bold;")
            l.setStyleSheet(f"color: {'#0088cc' if active else '#6c757d'}; font-weight: {'bold' if active else 'normal'};")

    def create_setup_page(self):
        p = QWidget(); l = QVBoxLayout(p); l.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card = QFrame(); card.setFixedWidth(500); card.setStyleSheet(f"background: {'#1e1e1e' if self.is_dark else 'white'}; border-radius: 15px; border: 1px solid {'#333' if self.is_dark else '#dee2e6'};")
        cl = QVBoxLayout(card); cl.setContentsMargins(40, 40, 40, 40); cl.setSpacing(20)
        cl.addWidget(QLabel("🔐", font=QFont("Arial", 40), alignment=Qt.AlignmentFlag.AlignCenter))
        cl.addWidget(QLabel(tr("setup_title"), font=QFont("Arial", 18, QFont.Weight.Bold), alignment=Qt.AlignmentFlag.AlignCenter))
        cl.addWidget(QLabel(tr("setup_instructions"), wordWrap=True, alignment=Qt.AlignmentFlag.AlignCenter))
        ob = QPushButton(tr("btn_open_telegram")); ob.setObjectName("primaryBtn"); ob.clicked.connect(lambda: webbrowser.open('https://my.telegram.org/apps')); cl.addWidget(ob)
        form = QFormLayout(); self.aid_in = QLineEdit(self.settings.value('api_id', '')); self.ah_in = QLineEdit(self.settings.value('api_hash', '')); self.ph_in = QLineEdit(self.settings.value('phone', ''))
        form.addRow(tr("label_api_id"), self.aid_in); form.addRow(tr("label_api_hash"), self.ah_in); form.addRow(tr("label_phone"), self.ph_in); cl.addLayout(form)
        sb = QPushButton(tr("btn_save_continue")); sb.setObjectName("successBtn"); sb.setFixedHeight(50); sb.clicked.connect(self.save_and_continue); cl.addWidget(sb); l.addWidget(card)
        return p

    def create_scan_page(self):
        p = QWidget(); l = QVBoxLayout(p); l.setContentsMargins(100, 50, 100, 50); l.setSpacing(20)
        l.addWidget(QLabel(tr("scan_title"), font=QFont("Arial", 20, QFont.Weight.Bold)))
        gb = QGroupBox(tr("scan_group_label")); gl = QVBoxLayout(gb); self.group_in = QLineEdit(); self.group_in.setPlaceholderText(tr("scan_group_placeholder")); self.group_in.setFixedHeight(50); gl.addWidget(self.group_in); l.addWidget(gb)
        ob = QGroupBox(tr("scan_options")); ol = QHBoxLayout(ob); ol.addWidget(QLabel(tr("scan_max_messages"))); self.max_spin = QSpinBox(); self.max_spin.setRange(10, 200000); self.max_spin.setValue(1000); ol.addWidget(self.max_spin); l.addWidget(ob)
        self.scan_st = QLabel(""); self.scan_st.setAlignment(Qt.AlignmentFlag.AlignCenter); l.addWidget(self.scan_st)
        self.scan_pr = QProgressBar(); self.scan_pr.setVisible(False); l.addWidget(self.scan_pr)
        self.scan_btn = QPushButton(tr("btn_start_scan")); self.scan_btn.setObjectName("primaryBtn"); self.scan_btn.setFixedHeight(60); self.scan_btn.clicked.connect(self.start_scan); l.addWidget(self.scan_btn)
        self.stop_scan_btn = QPushButton(tr("btn_stop_scan")); self.stop_scan_btn.setObjectName("dangerBtn"); self.stop_scan_btn.setVisible(False); self.stop_scan_btn.clicked.connect(self.stop_scan); l.addWidget(self.stop_scan_btn)
        l.addStretch(); return p

    def create_select_page(self):
        p = QWidget(); l = QVBoxLayout(p); l.setContentsMargins(30, 20, 30, 20)
        h = QHBoxLayout(); h.addWidget(QLabel(tr("select_title"), font=QFont("Arial", 18, QFont.Weight.Bold))); h.addStretch()
        sa = QPushButton(tr("btn_select_all")); sa.clicked.connect(self.select_all); h.addWidget(sa); sn = QPushButton(tr("btn_select_none")); sn.clicked.connect(self.select_none); h.addWidget(sn); l.addLayout(h)
        
        fl = QHBoxLayout(); fl.addWidget(QLabel(tr("filter_label"))); self.filter_cb = QComboBox(); self.filter_cb.addItems([tr("filter_all"), tr("filter_photos"), tr("filter_videos"), tr("filter_documents"), tr("filter_archives")]); self.filter_cb.currentTextChanged.connect(self.apply_filter); fl.addWidget(self.filter_cb)
        self.search_in = QLineEdit(); self.search_in.setPlaceholderText(tr("search_placeholder")); self.search_in.textChanged.connect(self.apply_filter); fl.addWidget(self.search_in)
        self.sel_lab = QLabel(tr("selected_count", count=0)); self.sel_lab.setStyleSheet("font-weight: bold; color: #0088cc;"); fl.addWidget(self.sel_lab); l.addLayout(fl)
        
        self.scroll = QScrollArea(); self.scroll.setWidgetResizable(True); self.cont = QWidget(); self.files_l = QVBoxLayout(self.cont); self.files_l.setSpacing(8); self.scroll.setWidget(self.cont); l.addWidget(self.scroll)
        path_l = QHBoxLayout(); path_l.addWidget(QLabel(tr("download_path_label"))); self.path_in = QLineEdit(str(Path.home() / "Downloads" / "Telegram")); path_l.addWidget(self.path_in); bb = QPushButton(tr("btn_browse")); bb.clicked.connect(self.browse_path); path_l.addWidget(bb); l.addWidget(QLabel(f"{tr('menu_settings')}: Parallel Downloads (3)")); l.addLayout(path_l)
        bl = QHBoxLayout(); back = QPushButton(tr("btn_back")); back.setFixedWidth(120); back.clicked.connect(self.show_scan_page); bl.addWidget(back); self.dl_btn = QPushButton(tr("btn_download_selected")); self.dl_btn.setObjectName("successBtn"); self.dl_btn.setFixedHeight(55); self.dl_btn.clicked.connect(self.start_download); bl.addWidget(self.dl_btn, 1); l.addLayout(bl)
        return p

    def create_download_page(self):
        p = QWidget(); l = QVBoxLayout(p); l.setAlignment(Qt.AlignmentFlag.AlignCenter); l.setSpacing(20)
        self.dl_st = QLabel(tr("download_starting"), font=QFont("Arial", 18, QFont.Weight.Bold)); l.addWidget(self.dl_st, 0, Qt.AlignmentFlag.AlignCenter)
        self.cur_f_lab = QLabel(""); l.addWidget(self.cur_f_lab, 0, Qt.AlignmentFlag.AlignCenter)
        self.dl_pr = QProgressBar(); self.dl_pr.setFixedWidth(600); l.addWidget(self.dl_pr, 0, Qt.AlignmentFlag.AlignCenter)
        self.stats_lab = QLabel(""); l.addWidget(self.stats_lab, 0, Qt.AlignmentFlag.AlignCenter)
        self.speed_lab = QLabel(""); self.speed_lab.setStyleSheet("color: #0088cc; font-weight: bold;"); l.addWidget(self.speed_lab, 0, Qt.AlignmentFlag.AlignCenter)
        self.stop_dl_btn = QPushButton(tr("btn_stop_download")); self.stop_dl_btn.setObjectName("dangerBtn"); self.stop_dl_btn.clicked.connect(self.stop_download); l.addWidget(self.stop_dl_btn, 0, Qt.AlignmentFlag.AlignCenter)
        done_l = QHBoxLayout(); self.done_b = QPushButton(tr("btn_done")); self.done_b.setObjectName("primaryBtn"); self.done_b.setFixedSize(180, 50); self.done_b.setVisible(False); self.done_b.clicked.connect(self.reset_to_scan); done_l.addWidget(self.done_b)
        self.open_f_b = QPushButton(tr("btn_open_folder")); self.open_f_b.setObjectName("successBtn"); self.open_f_b.setFixedSize(180, 50); self.open_f_b.setVisible(False); self.open_f_b.clicked.connect(self.open_folder); done_l.addWidget(self.open_f_b); l.addLayout(done_l)
        return p

    def show_setup_page(self): self.stack.setCurrentIndex(0); self.update_progress_step(1)
    def show_scan_page(self): self.stack.setCurrentIndex(1); self.update_progress_step(2)
    def show_select_page(self): self.stack.setCurrentIndex(2); self.update_progress_step(3)
    def show_download_page(self): self.stack.setCurrentIndex(3); self.update_progress_step(4)

    def save_and_continue(self):
        aid, ah, ph = self.aid_in.text().strip(), self.ah_in.text().strip(), self.ph_in.text().strip()
        if not all([aid, ah, ph]): return QMessageBox.warning(self, tr("error"), tr("error_empty_fields"))
        self.settings.setValue('api_id', aid); self.settings.setValue('api_hash', ah); self.settings.setValue('phone', ph)
        self.init_telegram_client(); self.show_scan_page()

    def init_telegram_client(self):
        self.aid, self.ah, self.ph = int(self.settings.value('api_id')), self.settings.value('api_hash'), self.settings.value('phone')
        self.sp = Path.home() / '.telegram_downloader' / 'session'; self.sp.parent.mkdir(exist_ok=True)
        self.at = AuthThread(self.aid, self.ah, self.sp, self.ph)
        self.at.code_needed.connect(self.handle_code_request); self.at.password_needed.connect(self.handle_password_request)
        self.at.auth_success.connect(self.handle_auth_success); self.at.auth_error.connect(self.handle_auth_error); self.at.start()

    def handle_code_request(self, ph):
        code, ok = QInputDialog.getText(self, tr("dialog_code_title"), tr("dialog_code_message", phone=ph))
        if ok: self.at.code = code
    def handle_password_request(self):
        pwd, ok = QInputDialog.getText(self, tr("dialog_password_title"), tr("dialog_password_message"), QLineEdit.EchoMode.Password)
        if ok: self.at.password = pwd
    def handle_auth_success(self): self.scan_st.setText(tr("scan_connected")); self.scan_st.setStyleSheet("color: #28a745; font-weight: bold;")
    def handle_auth_error(self, e): QMessageBox.critical(self, tr("error"), f"{tr('error_connection', error=e)}")

    def start_scan(self):
        l = self.group_in.text().strip()
        if not l: return QMessageBox.warning(self, tr("error"), tr("error_no_group"))
        self.scan_btn.setVisible(False); self.stop_scan_btn.setVisible(True); self.scan_pr.setVisible(True)
        self.st = ScanThread(self.aid, self.ah, self.sp, l, self.max_spin.value())
        self.st.progress.connect(self.update_scan_progress); self.st.content_found.connect(self.show_content); self.st.error.connect(self.scan_error); self.st.start()

    def stop_scan(self):
        if hasattr(self, 'st'): self.st.stop()
        self.reset_scan_ui()
    def reset_scan_ui(self): self.scan_btn.setVisible(True); self.stop_scan_btn.setVisible(False); self.scan_pr.setVisible(False)
    def update_scan_progress(self, p, s): self.scan_pr.setValue(p); self.scan_st.setText(s)
    def scan_error(self, e): self.reset_scan_ui(); QMessageBox.critical(self, tr("error"), f"{tr('error_scan', error=e)}")

    def show_content(self, items):
        self.reset_scan_ui()
        while self.files_l.count():
            c = self.files_l.takeAt(0)
            if c.widget(): c.widget().deleteLater()
        for item in items:
            w = MediaItemWidget(item, self.is_dark)
            w.changed.connect(self.update_selected_count)
            self.files_l.addWidget(w)
        self.files_l.addStretch(); self.update_selected_count(); self.show_select_page()

    def select_all(self):
        for i in range(self.files_l.count()):
            w = self.files_l.itemAt(i).widget()
            if isinstance(w, MediaItemWidget): w.set_checked(True)
        self.update_selected_count()
    def select_none(self):
        for i in range(self.files_l.count()):
            w = self.files_l.itemAt(i).widget()
            if isinstance(w, MediaItemWidget): w.set_checked(False)
        self.update_selected_count()
    def update_selected_count(self):
        count = sum(1 for i in range(self.files_l.count()) if isinstance(self.files_l.itemAt(i).widget(), MediaItemWidget) and self.files_l.itemAt(i).widget().is_checked())
        self.sel_lab.setText(tr("selected_count", count=count))

    def apply_filter(self):
        text = self.filter_cb.currentText()
        search = self.search_in.text().lower()
        mapping = {tr("filter_photos"): ["photo", "image"], tr("filter_videos"): ["video"], tr("filter_documents"): ["document"], tr("filter_archives"): ["archive"]}
        types = mapping.get(text, None)
        for i in range(self.files_l.count()):
            w = self.files_l.itemAt(i).widget()
            if isinstance(w, MediaItemWidget):
                type_match = types is None or w.item['type'] in types
                search_match = search in w.item['name'].lower()
                w.setVisible(type_match and search_match)

    def browse_path(self):
        path = QFileDialog.getExistingDirectory(self, tr("dialog_select_folder"))
        if path: self.path_in.setText(path)

    def start_download(self):
        items = [self.files_l.itemAt(i).widget().item for i in range(self.files_l.count()) if isinstance(self.files_l.itemAt(i).widget(), MediaItemWidget) and self.files_l.itemAt(i).widget().is_checked()]
        if not items: return QMessageBox.warning(self, tr("error"), tr("error_no_files_selected"))
        path = Path(self.path_in.text()); path.mkdir(parents=True, exist_ok=True)
        self.show_download_page()
        self.dt = ParallelDownloadThread(self.aid, self.ah, self.sp, items, path)
        self.dt.progress.connect(self.update_dl_progress); self.dt.finished.connect(self.dl_finished); self.dt.start()

    def update_dl_progress(self, p, f, c, t, speed, eta):
        self.dl_pr.setValue(p); self.cur_f_lab.setText(tr("download_current", filename=f)); self.stats_lab.setText(f"{tr('download_progress', current=c, total=t)} | {tr('download_eta', eta=eta)}"); self.speed_lab.setText(tr("download_speed", speed=speed))

    def dl_finished(self, d, f):
        self.stop_dl_btn.setVisible(False); self.done_b.setVisible(True); self.open_f_b.setVisible(True)
        self.dl_st.setText(tr("download_completed")); self.stats_lab.setText(tr("download_stats", downloaded=d, failed=f))
        # Notification (simplified for sandbox)
        print(f"NOTIFICATION: {tr('notify_title')} - {tr('notify_message', count=d)}")

    def stop_download(self):
        if hasattr(self, 'dt'): self.dt.stop()
    def reset_to_scan(self): self.show_scan_page(); self.done_b.setVisible(False); self.open_f_b.setVisible(False); self.stop_dl_btn.setVisible(True)
    def open_folder(self):
        p = self.path_in.text()
        if sys.platform == 'win32': os.startfile(p)
        elif sys.platform == 'darwin': subprocess.Popen(['open', p])
        else: subprocess.Popen(['xdg-open', p])

    def logout(self):
        if QMessageBox.question(self, tr("menu_settings"), tr("confirm_logout")) == QMessageBox.StandardButton.Yes:
            self.settings.clear(); QMessageBox.information(self, tr("success"), tr("success_logout")); self.show_setup_page()

    def show_about(self): QMessageBox.about(self, tr("about_title"), tr("about_text"))

def main():
    app = QApplication(sys.argv)
    if not TELETHON_AVAILABLE: return QMessageBox.critical(None, tr("error"), tr("error_telethon_missing")), 1
    window = ModernWindow(); window.show(); return app.exec()

if __name__ == '__main__': sys.exit(main())
