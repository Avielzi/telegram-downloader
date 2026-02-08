"""
Telegram Downloader - Uninstaller
מסיר התקנה - Telegram Downloader

Created by Aviel.AI
"""

import sys
import os
import shutil
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QCheckBox, QMessageBox, QProgressBar
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont


class UninstallThread(QThread):
    """Thread for performing uninstallation"""
    progress = pyqtSignal(int, str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, options):
        super().__init__()
        self.options = options
        
    def run(self):
        try:
            total_steps = sum([
                self.options['remove_app'],
                self.options['remove_settings'],
                self.options['remove_sessions'],
                self.options['remove_downloads'],
            ])
            
            current_step = 0
            
            # Step 1: Remove application files
            if self.options['remove_app']:
                self.progress.emit(int((current_step / total_steps) * 100), "מוחק קבצי תוכנה...")
                app_path = Path(__file__).parent
                
                # List of files to remove
                files_to_remove = [
                    'telegram_downloader.py',
                    'telegram_downloader_v2.py',
                    'i18n.py',
                    'requirements.txt',
                    'telegram_downloader.spec',
                    'uninstall.py',
                    'uninstall.bat',
                    '*.pyc',
                ]
                
                for pattern in files_to_remove:
                    if '*' in pattern:
                        for file in app_path.glob(pattern):
                            try:
                                file.unlink()
                            except:
                                pass
                    else:
                        file_path = app_path / pattern
                        if file_path.exists():
                            try:
                                file_path.unlink()
                            except:
                                pass
                
                # Remove __pycache__
                pycache = app_path / '__pycache__'
                if pycache.exists():
                    shutil.rmtree(pycache, ignore_errors=True)
                
                current_step += 1
            
            # Step 2: Remove settings
            if self.options['remove_settings']:
                self.progress.emit(int((current_step / total_steps) * 100), "מוחק הגדרות...")
                
                # QSettings location
                try:
                    from PyQt6.QtCore import QSettings
                    settings = QSettings('TelegramDownloader', 'Settings')
                    settings.clear()
                    settings.sync()
                except:
                    pass
                
                # Registry/config files (Windows)
                if sys.platform == 'win32':
                    config_paths = [
                        Path.home() / 'AppData' / 'Roaming' / 'TelegramDownloader',
                        Path.home() / 'AppData' / 'Local' / 'TelegramDownloader',
                    ]
                    for config_path in config_paths:
                        if config_path.exists():
                            shutil.rmtree(config_path, ignore_errors=True)
                
                current_step += 1
            
            # Step 3: Remove session files
            if self.options['remove_sessions']:
                self.progress.emit(int((current_step / total_steps) * 100), "מוחק קבצי session...")
                
                session_path = Path.home() / '.telegram_downloader'
                if session_path.exists():
                    shutil.rmtree(session_path, ignore_errors=True)
                
                current_step += 1
            
            # Step 4: Remove downloaded files
            if self.options['remove_downloads']:
                self.progress.emit(int((current_step / total_steps) * 100), "מוחק קבצים שהורדו...")
                
                # Default download location
                download_path = Path.home() / 'Downloads' / 'Telegram'
                if download_path.exists():
                    shutil.rmtree(download_path, ignore_errors=True)
                
                current_step += 1
            
            self.progress.emit(100, "ההסרה הושלמה!")
            self.finished.emit(True, "התוכנה הוסרה בהצלחה!")
            
        except Exception as e:
            self.finished.emit(False, f"שגיאה בהסרה: {str(e)}")


class UninstallerDialog(QDialog):
    """Uninstaller dialog window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("הסרת Telegram Downloader")
        self.setFixedSize(550, 600)
        self.setModal(True)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("🗑️ הסרת התקנה")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #f44336; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("נוצר על ידי Aviel.AI")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #666; font-size: 12px; margin-bottom: 20px;")
        layout.addWidget(subtitle)
        
        # Message
        message = QLabel("האם אתה בטוח שברצונך להסיר את Telegram Downloader?")
        message.setWordWrap(True)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setStyleSheet("font-size: 14px; margin-bottom: 20px;")
        layout.addWidget(message)
        
        # Options
        options_label = QLabel("🔧 בחר מה להסיר:")
        options_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        options_label.setStyleSheet("margin-top: 10px;")
        layout.addWidget(options_label)
        
        # Checkboxes
        self.cb_app = QCheckBox("קבצי התוכנה (telegram_downloader.py, i18n.py וכו')")
        self.cb_app.setChecked(True)
        self.cb_app.setStyleSheet("font-size: 13px; padding: 5px;")
        layout.addWidget(self.cb_app)
        
        self.cb_settings = QCheckBox("הגדרות (API credentials, העדפות)")
        self.cb_settings.setChecked(True)
        self.cb_settings.setStyleSheet("font-size: 13px; padding: 5px;")
        layout.addWidget(self.cb_settings)
        
        self.cb_sessions = QCheckBox("קבצי Session של טלגרם")
        self.cb_sessions.setChecked(True)
        self.cb_sessions.setStyleSheet("font-size: 13px; padding: 5px;")
        layout.addWidget(self.cb_sessions)
        
        self.cb_downloads = QCheckBox("קבצים שהורדו (בתיקייה Downloads/Telegram)")
        self.cb_downloads.setChecked(False)
        self.cb_downloads.setStyleSheet("font-size: 13px; padding: 5px; color: #f44336;")
        layout.addWidget(self.cb_downloads)
        
        # Warning for downloads
        warning = QLabel("⚠️ שים לב: סימון האפשרות האחרונה ימחק את כל הקבצים שהורדת!")
        warning.setWordWrap(True)
        warning.setStyleSheet("""
            background-color: #fff3cd;
            color: #856404;
            padding: 10px;
            border-radius: 5px;
            font-size: 11px;
            margin-top: 10px;
        """)
        layout.addWidget(warning)
        
        # Progress
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #ddd;
                border-radius: 5px;
                text-align: center;
                height: 25px;
            }
            QProgressBar::chunk {
                background-color: #f44336;
            }
        """)
        layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setVisible(False)
        self.status_label.setStyleSheet("color: #666; font-size: 12px;")
        layout.addWidget(self.status_label)
        
        # Info
        info_box = QLabel("""
        <div dir="rtl" style="font-family: Arial; font-size: 11px; color: #666;">
        <p><b>מה יקרה:</b></p>
        <ul>
            <li>קבצי התוכנה יימחקו</li>
            <li>ההגדרות שלך יימחקו (יצטרך להזין API מחדש)</li>
            <li>קבצי Session יימחקו (יצטרך להתחבר מחדש)</li>
            <li>התיקייה הראשית תישאר (תוכל למחוק ידנית)</li>
        </ul>
        </div>
        """)
        info_box.setWordWrap(True)
        info_box.setStyleSheet("""
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            margin-top: 10px;
        """)
        layout.addWidget(info_box)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.cancel_btn = QPushButton("ביטול")
        self.cancel_btn.setFixedHeight(45)
        self.cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 30px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_btn)
        
        self.uninstall_btn = QPushButton("🗑️ הסר התקנה")
        self.uninstall_btn.setFixedHeight(45)
        self.uninstall_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 30px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)
        self.uninstall_btn.clicked.connect(self.start_uninstall)
        button_layout.addWidget(self.uninstall_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
    def start_uninstall(self):
        # Confirm
        if self.cb_downloads.isChecked():
            reply = QMessageBox.warning(
                self,
                'אזהרה!',
                'אתה עומד למחוק גם את הקבצים שהורדת!\n\nהאם אתה בטוח?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.No:
                return
        
        # Final confirmation
        reply = QMessageBox.question(
            self,
            'אישור סופי',
            'האם אתה בטוח שברצונך להסיר את Telegram Downloader?\n\nפעולה זו לא ניתנת לביטול.',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.No:
            return
        
        # Disable UI
        self.uninstall_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.cb_app.setEnabled(False)
        self.cb_settings.setEnabled(False)
        self.cb_sessions.setEnabled(False)
        self.cb_downloads.setEnabled(False)
        
        # Show progress
        self.progress_bar.setVisible(True)
        self.status_label.setVisible(True)
        
        # Get options
        options = {
            'remove_app': self.cb_app.isChecked(),
            'remove_settings': self.cb_settings.isChecked(),
            'remove_sessions': self.cb_sessions.isChecked(),
            'remove_downloads': self.cb_downloads.isChecked(),
        }
        
        # Start uninstall
        self.uninstall_thread = UninstallThread(options)
        self.uninstall_thread.progress.connect(self.update_progress)
        self.uninstall_thread.finished.connect(self.uninstall_finished)
        self.uninstall_thread.start()
    
    def update_progress(self, value, status):
        self.progress_bar.setValue(value)
        self.status_label.setText(status)
    
    def uninstall_finished(self, success, message):
        self.progress_bar.setVisible(False)
        self.status_label.setVisible(False)
        
        if success:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("הצלחה")
            msg.setText(message)
            msg.setInformativeText(
                "התוכנה הוסרה מהמחשב.\n\n"
                "תיקיית ההתקנה עצמה עדיין קיימת.\n"
                "תוכל למחוק אותה ידנית אם תרצה.\n\n"
                "תודה שהשתמשת ב-Telegram Downloader!\n\n"
                "נוצר על ידי Aviel.AI ❤️"
            )
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            
            self.accept()
        else:
            QMessageBox.critical(self, "שגיאה", message)
            self.uninstall_btn.setEnabled(True)
            self.cancel_btn.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    
    # Set style
    app.setStyle('Fusion')
    
    dialog = UninstallerDialog()
    result = dialog.exec()
    
    return result


if __name__ == '__main__':
    sys.exit(main())
