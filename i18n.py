"""
Internationalization (i18n) support for Telegram Downloader ULTIMATE PRO
Created by Aviel.AI
"""

import json
from pathlib import Path
from typing import Dict, Optional

class Translation:
    def __init__(self, language: str = "he"):
        self.current_language = language
        self.translations: Dict[str, Dict] = {}
        self.load_translations()
    
    def load_translations(self):
        self.translations = BUILT_IN_TRANSLATIONS.copy()
        translations_dir = Path(__file__).parent / "translations"
        if translations_dir.exists():
            for file in translations_dir.glob("*.json"):
                lang_code = file.stem
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        file_translations = json.load(f)
                        if lang_code in self.translations:
                            self.translations[lang_code].update(file_translations)
                        else:
                            self.translations[lang_code] = file_translations
                except Exception: continue
    
    def get(self, key: str, **kwargs) -> str:
        translation = self.translations.get(self.current_language, {}).get(key, key)
        if kwargs:
            try: return translation.format(**kwargs)
            except (KeyError, ValueError): return translation
        return translation
    
    def set_language(self, language: str):
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get_available_languages(self) -> Dict[str, str]:
        return {lang: self.translations[lang].get("language_name", lang) for lang in self.translations.keys()}

BUILT_IN_TRANSLATIONS = {
    "en": {
        "language_name": "English",
        "app_name": "Telegram Downloader",
        "app_version": "v2.3.0 ULTIMATE PRO",
        "menu_settings": "Settings",
        "menu_language": "Language",
        "menu_about": "About",
        "menu_theme": "Theme",
        "theme_light": "Light Mode",
        "theme_dark": "Dark Mode",
        "step_setup": "Setup",
        "step_scan": "Scan",
        "step_select": "Select",
        "step_download": "Download",
        "setup_title": "Telegram ULTIMATE PRO Setup",
        "setup_instructions": "Connect your Telegram account securely to begin.",
        "btn_open_telegram": "🌐 Get API Credentials",
        "label_api_id": "API ID",
        "label_api_hash": "API Hash",
        "label_phone": "Phone Number",
        "btn_save_continue": "Save & Connect →",
        "scan_title": "Deep Scan Media",
        "scan_group_label": "Group/Channel Link",
        "scan_group_placeholder": "https://t.me/groupname or @groupname",
        "scan_options": "Scan Settings",
        "scan_max_messages": "Scan Limit",
        "btn_start_scan": "🔍 Start Deep Scan",
        "btn_stop_scan": "⏹ Stop",
        "scan_connecting": "Connecting...",
        "scan_connected": "✓ Secure Connection Established",
        "scan_scanning": "Scanning messages...",
        "scan_found_files": "Found {count} files",
        "select_title": "Select Media Assets",
        "btn_select_all": "Select All",
        "btn_select_none": "Deselect All",
        "filter_label": "Type:",
        "filter_all": "All Files",
        "filter_photos": "Photos",
        "filter_videos": "Videos",
        "filter_documents": "Documents",
        "filter_archives": "Archives",
        "search_placeholder": "Search by filename...",
        "selected_count": "{count} Files Selected",
        "download_path_label": "Download to:",
        "btn_browse": "Browse",
        "btn_back": "Back",
        "btn_download_selected": "⬇ Download Selected ULTIMATE",
        "download_starting": "Initializing Engine...",
        "download_current": "Downloading: {filename}",
        "download_progress": "{current} / {total}",
        "download_speed": "Speed: {speed}",
        "download_eta": "ETA: {eta}",
        "download_completed": "✓ ULTIMATE Download Successful!",
        "download_stats": "Downloaded: {downloaded} • Failed: {failed}",
        "btn_stop_download": "Cancel",
        "btn_done": "Finish",
        "btn_open_folder": "Open Folder",
        "dialog_code_title": "Auth Code",
        "dialog_code_message": "Enter the code sent to {phone}:",
        "dialog_password_title": "2FA Required",
        "dialog_password_message": "Enter your 2FA password:",
        "dialog_select_folder": "Select Destination",
        "error": "Error",
        "success": "Success",
        "notify_title": "Download Complete",
        "notify_message": "Successfully downloaded {count} files to your computer.",
        "error_empty_fields": "All fields are required",
        "error_no_group": "Enter a valid link",
        "error_no_files_selected": "No files selected",
        "error_connection": "Connection failed: {error}",
        "error_scan": "Scan failed: {error}",
        "success_logout": "Logged out",
        "about_title": "About ULTIMATE PRO",
        "about_text": "<h2>Telegram Downloader ULTIMATE PRO</h2><p>The most advanced media retrieval engine.</p><p>Built with ❤️ by Aviel.AI</p>"
    },
    "he": {
        "language_name": "עברית",
        "app_name": "מוריד טלגרם",
        "app_version": "גרסה 2.3.0 ULTIMATE PRO",
        "menu_settings": "הגדרות",
        "menu_language": "שפה",
        "menu_about": "אודות",
        "menu_theme": "ערכת נושא",
        "theme_light": "מצב בהיר",
        "theme_dark": "מצב כהה",
        "step_setup": "הגדרה",
        "step_scan": "סריקה",
        "step_select": "בחירה",
        "step_download": "הורדה",
        "setup_title": "הגדרת ULTIMATE PRO",
        "setup_instructions": "חבר את חשבון הטלגרם שלך בצורה מאובטחת כדי להתחיל.",
        "btn_open_telegram": "🌐 קבלת אישורי API",
        "label_api_id": "API ID",
        "label_api_hash": "API Hash",
        "label_phone": "מספר טלפון",
        "btn_save_continue": "שמור והתחבר ←",
        "scan_title": "סריקת מדיה עמוקה",
        "scan_group_label": "קישור לקבוצה/ערוץ",
        "scan_group_placeholder": "https://t.me/groupname או @groupname",
        "scan_options": "הגדרות סריקה",
        "scan_max_messages": "הגבלת סריקה",
        "btn_start_scan": "🔍 התחל סריקה עמוקה",
        "btn_stop_scan": "⏹ עצור",
        "scan_connecting": "מתחבר...",
        "scan_connected": "✓ חיבור מאובטח נוצר",
        "scan_scanning": "סורק הודעות...",
        "scan_found_files": "נמצאו {count} קבצים",
        "select_title": "בחירת נכסי מדיה",
        "btn_select_all": "בחר הכל",
        "btn_select_none": "בטל הכל",
        "filter_label": "סוג:",
        "filter_all": "כל הקבצים",
        "filter_photos": "תמונות",
        "filter_videos": "וידאו",
        "filter_documents": "מסמכים",
        "filter_archives": "ארכיונים",
        "search_placeholder": "חיפוש לפי שם קובץ...",
        "selected_count": "{count} קבצים נבחרו",
        "download_path_label": "הורדה ל:",
        "btn_browse": "עיון",
        "btn_back": "חזור",
        "btn_download_selected": "⬇ הורד קבצים ULTIMATE",
        "download_starting": "מפעיל מנוע הורדה...",
        "download_current": "מוריד: {filename}",
        "download_progress": "{current} מתוך {total}",
        "download_speed": "מהירות: {speed}",
        "download_eta": "זמן נותר: {eta}",
        "download_completed": "✓ הורדת ULTIMATE הושלמה בהצלחה!",
        "download_stats": "הורדו: {downloaded} • נכשלו: {failed}",
        "btn_stop_download": "ביטול",
        "btn_done": "סיום",
        "btn_open_folder": "פתח תיקייה",
        "dialog_code_title": "קוד אימות",
        "dialog_code_message": "הזן את הקוד שנשלח ל-{phone}:",
        "dialog_password_title": "נדרש 2FA",
        "dialog_password_message": "הזן סיסמת אימות דו-שלבי:",
        "dialog_select_folder": "בחר תיקיית יעד",
        "error": "שגיאה",
        "success": "הצלחה",
        "notify_title": "ההורדה הושלמה",
        "notify_message": "בהצלחה הורדו {count} קבצים למחשב שלך.",
        "error_empty_fields": "כל השדות הם חובה",
        "error_no_group": "הזן קישור תקין",
        "error_no_files_selected": "לא נבחרו קבצים",
        "error_connection": "החיבור נכשל: {error}",
        "error_scan": "הסריקה נכשלה: {error}",
        "success_logout": "התנתקת בהצלחה",
        "about_title": "אודות ULTIMATE PRO",
        "about_text": "<h2>מוריד טלגרם ULTIMATE PRO</h2><p>מנוע הורדת המדיה המתקדם ביותר.</p><p>נבנה באהבה על ידי Aviel.AI</p>"
    }
}

_translator: Optional[Translation] = None
def get_translator() -> Translation:
    global _translator
    if _translator is None: _translator = Translation()
    return _translator
def tr(key: str, **kwargs) -> str: return get_translator().get(key, **kwargs)
