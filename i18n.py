"""
Internationalization (i18n) support for Telegram Downloader
Created by Aviel.AI
"""

import json
from pathlib import Path
from typing import Dict, Optional

class Translation:
    """Manages translations for the application"""
    
    def __init__(self, language: str = "en"):
        self.current_language = language
        self.translations: Dict[str, Dict] = {}
        self.load_translations()
    
    def load_translations(self):
        """Load all available translations"""
        translations_dir = Path(__file__).parent / "translations"
        
        if not translations_dir.exists():
            # Use built-in translations
            self.translations = BUILT_IN_TRANSLATIONS
        else:
            # Load from files
            for file in translations_dir.glob("*.json"):
                lang_code = file.stem
                with open(file, 'r', encoding='utf-8') as f:
                    self.translations[lang_code] = json.load(f)
    
    def get(self, key: str, **kwargs) -> str:
        """Get translated string"""
        translation = self.translations.get(self.current_language, {}).get(key, key)
        
        # Format with kwargs if provided
        if kwargs:
            try:
                return translation.format(**kwargs)
            except KeyError:
                return translation
        
        return translation
    
    def set_language(self, language: str):
        """Change current language"""
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get_available_languages(self) -> Dict[str, str]:
        """Get list of available languages"""
        return {
            lang: self.translations[lang].get("language_name", lang)
            for lang in self.translations.keys()
        }


# Built-in translations
BUILT_IN_TRANSLATIONS = {
    "en": {
        "language_name": "English",
        "language_code": "en",
        
        # App info
        "app_name": "Telegram Downloader",
        "app_version": "v2.0",
        "created_by": "Created by Aviel.AI",
        "license": "MIT License - Free & Open Source",
        
        # Menu
        "menu_settings": "Settings",
        "menu_language": "Language",
        "menu_about": "About",
        "menu_help": "Help",
        
        # Steps
        "step_setup": "Setup",
        "step_scan": "Scan",
        "step_select": "Select",
        "step_download": "Download",
        
        # Setup page
        "setup_title": "Telegram Connection Setup",
        "setup_instructions": """
        <div style="text-align: center; font-family: Arial;">
        <p><b>Click the button below to get API credentials</b></p>
        <p>You'll be asked to log in to Telegram and get identification numbers</p>
        </div>
        """,
        "btn_open_telegram": "🌐 Open my.telegram.org",
        "label_api_id": "API ID:",
        "label_api_hash": "API Hash:",
        "label_phone": "Phone:",
        "placeholder_api_id": "12345678",
        "placeholder_api_hash": "a1b2c3d4...",
        "placeholder_phone": "+1234567890",
        "btn_save_continue": "Save & Continue →",
        
        # Scan page
        "scan_title": "Scan Group/Channel",
        "scan_group_label": "Group link",
        "scan_group_placeholder": "https://t.me/groupname or @groupname",
        "scan_options": "Scan options",
        "scan_max_messages": "Number of messages to scan:",
        "btn_start_scan": "🔍 Start Scan",
        "btn_stop_scan": "⏹ Stop",
        "scan_connecting": "Connecting to Telegram...",
        "scan_connected": "✓ Connected to Telegram successfully!",
        "scan_searching": "Searching for group...",
        "scan_found_group": "Connected to: {name}",
        "scan_scanning": "Scanning messages...",
        "scan_found_messages": "Found {count} messages",
        "scan_analyzing": "Analyzing content...",
        "scan_found_files": "Found {count} files",
        
        # Select page
        "select_title": "Select Files to Download",
        "btn_select_all": "✓ Select All",
        "btn_select_none": "✗ Deselect All",
        "filter_label": "Filter:",
        "filter_all": "All",
        "filter_photos": "Photos",
        "filter_videos": "Videos",
        "filter_documents": "Documents",
        "filter_archives": "Archives",
        "selected_count": "Selected: {count} files",
        "download_path_label": "Destination folder:",
        "btn_browse": "📁 Browse...",
        "btn_back": "← Back",
        "btn_download_selected": "⬇ Download Selected Files",
        
        # Download page
        "download_starting": "Starting download...",
        "download_downloading": "Downloading files...",
        "download_current": "Downloading: {filename}",
        "download_progress": "File {current} of {total}",
        "download_completed": "✓ Download Completed!",
        "download_stats": "Downloaded {downloaded} files • Failed {failed}",
        "btn_stop_download": "⏹ Stop Download",
        "btn_done": "✓ Done",
        
        # Dialogs
        "dialog_code_title": "Verification Code",
        "dialog_code_message": "A verification code was sent to:\n{phone}\n\nPlease enter the code you received in Telegram:",
        "dialog_password_title": "Two-Factor Authentication (2FA)",
        "dialog_password_message": "Your account is protected with 2FA.\n\nPlease enter your password:",
        "dialog_select_folder": "Select destination folder",
        
        # Messages
        "error": "Error",
        "success": "Success",
        "warning": "Warning",
        "info": "Information",
        "error_empty_fields": "Please fill in all fields",
        "error_phone_format": "Phone number must start with +",
        "error_api_id_format": "API ID must be a number",
        "error_api_hash_format": "API Hash must be 32 characters",
        "error_no_group": "Please enter a group link",
        "error_no_files_selected": "No files selected",
        "error_telethon_missing": "Telethon library is not installed.\nPlease install: pip install telethon",
        "error_connection": "Connection error:\n{error}",
        "error_scan": "Scan error:\n{error}",
        "success_saved": "Settings saved successfully!",
        "confirm_logout": "Are you sure you want to log out?",
        "success_logout": "Logged out successfully",
        
        # About dialog
        "about_title": "About Telegram Downloader",
        "about_text": """
        <h2>Telegram Downloader v2.0</h2>
        <p><b>Created by: Aviel.AI</b></p>
        <p>An open-source tool for downloading media from Telegram groups and channels</p>
        <br>
        <p><b>Features:</b></p>
        <ul>
            <li>Bulk download media files</li>
            <li>Smart scanning and filtering</li>
            <li>Modern, intuitive interface</li>
            <li>Multi-language support</li>
        </ul>
        <br>
        <p><b>License:</b> MIT - Free & Open Source</p>
        <p><b>GitHub:</b> github.com/avielai/telegram-downloader</p>
        <br>
        <p>Built with ❤️ using Python, PyQt6, and Telethon</p>
        """,
        
        # File types
        "type_photo": "Photo",
        "type_image": "Image",
        "type_video": "Video",
        "type_document": "Document",
        "type_archive": "Archive",
        "type_file": "File",
    },
    
    "he": {
        "language_name": "עברית",
        "language_code": "he",
        
        # App info
        "app_name": "מוריד טלגרם",
        "app_version": "גרסה 2.0",
        "created_by": "נוצר על ידי Aviel.AI",
        "license": "רישיון MIT - חינמי וקוד פתוח",
        
        # Menu
        "menu_settings": "הגדרות",
        "menu_language": "שפה",
        "menu_about": "אודות",
        "menu_help": "עזרה",
        
        # Steps
        "step_setup": "הגדרות",
        "step_scan": "סריקה",
        "step_select": "בחירה",
        "step_download": "הורדה",
        
        # Setup page
        "setup_title": "הגדרת חיבור לטלגרם",
        "setup_instructions": """
        <div dir="rtl" style="text-align: center; font-family: Arial;">
        <p><b>לחץ על הכפתור למטה לקבלת אישורי API</b></p>
        <p>תתבקש להתחבר לטלגרם ולקבל מספרי זיהוי</p>
        </div>
        """,
        "btn_open_telegram": "🌐 פתח את my.telegram.org",
        "label_api_id": "API ID:",
        "label_api_hash": "API Hash:",
        "label_phone": "טלפון:",
        "placeholder_api_id": "12345678",
        "placeholder_api_hash": "a1b2c3d4...",
        "placeholder_phone": "+972501234567",
        "btn_save_continue": "שמור והמשך →",
        
        # Scan page
        "scan_title": "סריקת קבוצה/ערוץ",
        "scan_group_label": "קישור לקבוצה",
        "scan_group_placeholder": "https://t.me/groupname או @groupname",
        "scan_options": "אפשרויות סריקה",
        "scan_max_messages": "מספר הודעות לסריקה:",
        "btn_start_scan": "🔍 התחל סריקה",
        "btn_stop_scan": "⏹ עצור",
        "scan_connecting": "מתחבר לטלגרם...",
        "scan_connected": "✓ מחובר לטלגרם בהצלחה!",
        "scan_searching": "מחפש קבוצה...",
        "scan_found_group": "התחבר ל: {name}",
        "scan_scanning": "סורק הודעות...",
        "scan_found_messages": "נמצאו {count} הודעות",
        "scan_analyzing": "מנתח תוכן...",
        "scan_found_files": "נמצאו {count} קבצים",
        
        # Select page
        "select_title": "בחר קבצים להורדה",
        "btn_select_all": "✓ בחר הכל",
        "btn_select_none": "✗ בטל הכל",
        "filter_label": "סינון:",
        "filter_all": "הכל",
        "filter_photos": "תמונות",
        "filter_videos": "וידאו",
        "filter_documents": "מסמכים",
        "filter_archives": "ארכיונים",
        "selected_count": "נבחרו: {count} קבצים",
        "download_path_label": "תיקיית יעד:",
        "btn_browse": "📁 עיון...",
        "btn_back": "← חזור",
        "btn_download_selected": "⬇ הורד קבצים נבחרים",
        
        # Download page
        "download_starting": "מתחיל הורדה...",
        "download_downloading": "מוריד קבצים...",
        "download_current": "מוריד: {filename}",
        "download_progress": "קובץ {current} מתוך {total}",
        "download_completed": "✓ ההורדה הושלמה!",
        "download_stats": "הורדו {downloaded} קבצים • נכשלו {failed}",
        "btn_stop_download": "⏹ עצור הורדה",
        "btn_done": "✓ סיום",
        
        # Dialogs
        "dialog_code_title": "קוד אימות",
        "dialog_code_message": "נשלח קוד אימות ל:\n{phone}\n\nנא להזין את הקוד שקיבלת בטלגרם:",
        "dialog_password_title": "אימות דו-שלבי (2FA)",
        "dialog_password_message": "החשבון שלך מוגן באימות דו-שלבי.\n\nנא להזין את הסיסמה:",
        "dialog_select_folder": "בחר תיקיית יעד",
        
        # Messages
        "error": "שגיאה",
        "success": "הצלחה",
        "warning": "אזהרה",
        "info": "מידע",
        "error_empty_fields": "נא למלא את כל השדות",
        "error_phone_format": "מספר הטלפון חייב להתחיל ב-+",
        "error_api_id_format": "API ID חייב להיות מספר",
        "error_api_hash_format": "API Hash חייב להיות בן 32 תווים",
        "error_no_group": "נא להזין קישור לקבוצה",
        "error_no_files_selected": "לא נבחרו קבצים",
        "error_telethon_missing": "הספרייה Telethon לא מותקנת.\nנא להתקין: pip install telethon",
        "error_connection": "שגיאת חיבור:\n{error}",
        "error_scan": "שגיאת סריקה:\n{error}",
        "success_saved": "ההגדרות נשמרו בהצלחה!",
        "confirm_logout": "האם אתה בטוח שברצונך להתנתק?",
        "success_logout": "התנתקת בהצלחה",
        
        # About dialog
        "about_title": "אודות מוריד טלגרם",
        "about_text": """
        <div dir="rtl">
        <h2>מוריד טלגרם גרסה 2.0</h2>
        <p><b>נוצר על ידי: Aviel.AI</b></p>
        <p>כלי קוד פתוח להורדת מדיה מקבוצות וערוצי טלגרם</p>
        <br>
        <p><b>תכונות:</b></p>
        <ul>
            <li>הורדה המונית של קבצי מדיה</li>
            <li>סריקה וסינון חכם</li>
            <li>ממשק מודרני ואינטואיטיבי</li>
            <li>תמיכה בריבוי שפות</li>
        </ul>
        <br>
        <p><b>רישיון:</b> MIT - חינמי וקוד פתוח</p>
        <p><b>GitHub:</b> github.com/avielai/telegram-downloader</p>
        <br>
        <p>נבנה באהבה ❤️ באמצעות Python, PyQt6 ו-Telethon</p>
        </div>
        """,
        
        # File types
        "type_photo": "תמונה",
        "type_image": "תמונה",
        "type_video": "וידאו",
        "type_document": "מסמך",
        "type_archive": "ארכיון",
        "type_file": "קובץ",
    },
    
    "es": {
        "language_name": "Español",
        "language_code": "es",
        
        # App info
        "app_name": "Descargador de Telegram",
        "app_version": "v2.0",
        "created_by": "Creado por Aviel.AI",
        "license": "Licencia MIT - Gratis y de Código Abierto",
        
        # Menu
        "menu_settings": "Configuración",
        "menu_language": "Idioma",
        "menu_about": "Acerca de",
        "menu_help": "Ayuda",
        
        # Steps
        "step_setup": "Configuración",
        "step_scan": "Escanear",
        "step_select": "Seleccionar",
        "step_download": "Descargar",
        
        # Setup page
        "setup_title": "Configuración de Conexión a Telegram",
        "setup_instructions": """
        <div style="text-align: center; font-family: Arial;">
        <p><b>Haga clic en el botón a continuación para obtener credenciales API</b></p>
        <p>Se le pedirá que inicie sesión en Telegram y obtenga números de identificación</p>
        </div>
        """,
        "btn_open_telegram": "🌐 Abrir my.telegram.org",
        "label_api_id": "API ID:",
        "label_api_hash": "API Hash:",
        "label_phone": "Teléfono:",
        "placeholder_api_id": "12345678",
        "placeholder_api_hash": "a1b2c3d4...",
        "placeholder_phone": "+34612345678",
        "btn_save_continue": "Guardar y Continuar →",
        
        # Scan page
        "scan_title": "Escanear Grupo/Canal",
        "scan_group_label": "Enlace del grupo",
        "scan_group_placeholder": "https://t.me/groupname o @groupname",
        "scan_options": "Opciones de escaneo",
        "scan_max_messages": "Número de mensajes a escanear:",
        "btn_start_scan": "🔍 Iniciar Escaneo",
        "btn_stop_scan": "⏹ Detener",
        "scan_connecting": "Conectando a Telegram...",
        "scan_connected": "✓ ¡Conectado a Telegram exitosamente!",
        "scan_searching": "Buscando grupo...",
        "scan_found_group": "Conectado a: {name}",
        "scan_scanning": "Escaneando mensajes...",
        "scan_found_messages": "Se encontraron {count} mensajes",
        "scan_analyzing": "Analizando contenido...",
        "scan_found_files": "Se encontraron {count} archivos",
        
        # Select page
        "select_title": "Seleccionar Archivos para Descargar",
        "btn_select_all": "✓ Seleccionar Todo",
        "btn_select_none": "✗ Deseleccionar Todo",
        "filter_label": "Filtrar:",
        "filter_all": "Todo",
        "filter_photos": "Fotos",
        "filter_videos": "Videos",
        "filter_documents": "Documentos",
        "filter_archives": "Archivos",
        "selected_count": "Seleccionados: {count} archivos",
        "download_path_label": "Carpeta de destino:",
        "btn_browse": "📁 Examinar...",
        "btn_back": "← Atrás",
        "btn_download_selected": "⬇ Descargar Archivos Seleccionados",
        
        # Download page
        "download_starting": "Iniciando descarga...",
        "download_downloading": "Descargando archivos...",
        "download_current": "Descargando: {filename}",
        "download_progress": "Archivo {current} de {total}",
        "download_completed": "✓ ¡Descarga Completada!",
        "download_stats": "Descargados {downloaded} archivos • Fallados {failed}",
        "btn_stop_download": "⏹ Detener Descarga",
        "btn_done": "✓ Listo",
        
        # Dialogs
        "dialog_code_title": "Código de Verificación",
        "dialog_code_message": "Se envió un código de verificación a:\n{phone}\n\nPor favor, ingrese el código que recibió en Telegram:",
        "dialog_password_title": "Autenticación de Dos Factores (2FA)",
        "dialog_password_message": "Su cuenta está protegida con 2FA.\n\nPor favor, ingrese su contraseña:",
        "dialog_select_folder": "Seleccionar carpeta de destino",
        
        # Messages
        "error": "Error",
        "success": "Éxito",
        "warning": "Advertencia",
        "info": "Información",
        "error_empty_fields": "Por favor complete todos los campos",
        "error_phone_format": "El número de teléfono debe comenzar con +",
        "error_api_id_format": "API ID debe ser un número",
        "error_api_hash_format": "API Hash debe tener 32 caracteres",
        "error_no_group": "Por favor ingrese un enlace de grupo",
        "error_no_files_selected": "No se seleccionaron archivos",
        "error_telethon_missing": "La biblioteca Telethon no está instalada.\nPor favor instale: pip install telethon",
        "error_connection": "Error de conexión:\n{error}",
        "error_scan": "Error de escaneo:\n{error}",
        "success_saved": "¡Configuración guardada exitosamente!",
        "confirm_logout": "¿Está seguro de que desea cerrar sesión?",
        "success_logout": "Sesión cerrada exitosamente",
        
        # About dialog
        "about_title": "Acerca de Descargador de Telegram",
        "about_text": """
        <h2>Descargador de Telegram v2.0</h2>
        <p><b>Creado por: Aviel.AI</b></p>
        <p>Una herramienta de código abierto para descargar medios de grupos y canales de Telegram</p>
        <br>
        <p><b>Características:</b></p>
        <ul>
            <li>Descarga masiva de archivos multimedia</li>
            <li>Escaneo y filtrado inteligente</li>
            <li>Interfaz moderna e intuitiva</li>
            <li>Soporte multiidioma</li>
        </ul>
        <br>
        <p><b>Licencia:</b> MIT - Gratis y de Código Abierto</p>
        <p><b>GitHub:</b> github.com/avielai/telegram-downloader</p>
        <br>
        <p>Construido con ❤️ usando Python, PyQt6 y Telethon</p>
        """,
        
        # File types
        "type_photo": "Foto",
        "type_image": "Imagen",
        "type_video": "Video",
        "type_document": "Documento",
        "type_archive": "Archivo",
        "type_file": "Archivo",
    },
    
    "ru": {
        "language_name": "Русский",
        "language_code": "ru",
        
        # App info
        "app_name": "Загрузчик Telegram",
        "app_version": "v2.0",
        "created_by": "Создано Aviel.AI",
        "license": "Лицензия MIT - Бесплатно и с Открытым Кодом",
        
        # Menu
        "menu_settings": "Настройки",
        "menu_language": "Язык",
        "menu_about": "О программе",
        "menu_help": "Помощь",
        
        # Steps
        "step_setup": "Настройка",
        "step_scan": "Сканирование",
        "step_select": "Выбор",
        "step_download": "Загрузка",
        
        # Setup page
        "setup_title": "Настройка Подключения к Telegram",
        "setup_instructions": """
        <div style="text-align: center; font-family: Arial;">
        <p><b>Нажмите кнопку ниже, чтобы получить учетные данные API</b></p>
        <p>Вам будет предложено войти в Telegram и получить идентификационные номера</p>
        </div>
        """,
        "btn_open_telegram": "🌐 Открыть my.telegram.org",
        "label_api_id": "API ID:",
        "label_api_hash": "API Hash:",
        "label_phone": "Телефон:",
        "placeholder_api_id": "12345678",
        "placeholder_api_hash": "a1b2c3d4...",
        "placeholder_phone": "+79001234567",
        "btn_save_continue": "Сохранить и Продолжить →",
        
        # Scan page
        "scan_title": "Сканирование Группы/Канала",
        "scan_group_label": "Ссылка на группу",
        "scan_group_placeholder": "https://t.me/groupname или @groupname",
        "scan_options": "Параметры сканирования",
        "scan_max_messages": "Количество сообщений для сканирования:",
        "btn_start_scan": "🔍 Начать Сканирование",
        "btn_stop_scan": "⏹ Остановить",
        "scan_connecting": "Подключение к Telegram...",
        "scan_connected": "✓ Успешно подключено к Telegram!",
        "scan_searching": "Поиск группы...",
        "scan_found_group": "Подключено к: {name}",
        "scan_scanning": "Сканирование сообщений...",
        "scan_found_messages": "Найдено {count} сообщений",
        "scan_analyzing": "Анализ контента...",
        "scan_found_files": "Найдено {count} файлов",
        
        # Select page
        "select_title": "Выбрать Файлы для Загрузки",
        "btn_select_all": "✓ Выбрать Все",
        "btn_select_none": "✗ Снять Выбор",
        "filter_label": "Фильтр:",
        "filter_all": "Все",
        "filter_photos": "Фото",
        "filter_videos": "Видео",
        "filter_documents": "Документы",
        "filter_archives": "Архивы",
        "selected_count": "Выбрано: {count} файлов",
        "download_path_label": "Папка назначения:",
        "btn_browse": "📁 Обзор...",
        "btn_back": "← Назад",
        "btn_download_selected": "⬇ Загрузить Выбранные Файлы",
        
        # Download page
        "download_starting": "Начало загрузки...",
        "download_downloading": "Загрузка файлов...",
        "download_current": "Загрузка: {filename}",
        "download_progress": "Файл {current} из {total}",
        "download_completed": "✓ Загрузка Завершена!",
        "download_stats": "Загружено {downloaded} файлов • Ошибок {failed}",
        "btn_stop_download": "⏹ Остановить Загрузку",
        "btn_done": "✓ Готово",
        
        # Dialogs
        "dialog_code_title": "Код Подтверждения",
        "dialog_code_message": "Код подтверждения отправлен на:\n{phone}\n\nПожалуйста, введите код, полученный в Telegram:",
        "dialog_password_title": "Двухфакторная Аутентификация (2FA)",
        "dialog_password_message": "Ваша учетная запись защищена 2FA.\n\nПожалуйста, введите ваш пароль:",
        "dialog_select_folder": "Выберите папку назначения",
        
        # Messages
        "error": "Ошибка",
        "success": "Успех",
        "warning": "Предупреждение",
        "info": "Информация",
        "error_empty_fields": "Пожалуйста, заполните все поля",
        "error_phone_format": "Номер телефона должен начинаться с +",
        "error_api_id_format": "API ID должен быть числом",
        "error_api_hash_format": "API Hash должен содержать 32 символа",
        "error_no_group": "Пожалуйста, введите ссылку на группу",
        "error_no_files_selected": "Файлы не выбраны",
        "error_telethon_missing": "Библиотека Telethon не установлена.\nПожалуйста, установите: pip install telethon",
        "error_connection": "Ошибка подключения:\n{error}",
        "error_scan": "Ошибка сканирования:\n{error}",
        "success_saved": "Настройки успешно сохранены!",
        "confirm_logout": "Вы уверены, что хотите выйти?",
        "success_logout": "Выход выполнен успешно",
        
        # About dialog
        "about_title": "О Загрузчике Telegram",
        "about_text": """
        <h2>Загрузчик Telegram v2.0</h2>
        <p><b>Создано: Aviel.AI</b></p>
        <p>Инструмент с открытым исходным кодом для загрузки медиа из групп и каналов Telegram</p>
        <br>
        <p><b>Возможности:</b></p>
        <ul>
            <li>Массовая загрузка медиафайлов</li>
            <li>Умное сканирование и фильтрация</li>
            <li>Современный, интуитивный интерфейс</li>
            <li>Поддержка нескольких языков</li>
        </ul>
        <br>
        <p><b>Лицензия:</b> MIT - Бесплатно и с Открытым Кодом</p>
        <p><b>GitHub:</b> github.com/avielai/telegram-downloader</p>
        <br>
        <p>Создано с ❤️ используя Python, PyQt6 и Telethon</p>
        """,
        
        # File types
        "type_photo": "Фото",
        "type_image": "Изображение",
        "type_video": "Видео",
        "type_document": "Документ",
        "type_archive": "Архив",
        "type_file": "Файл",
    },
    
    "ar": {
        "language_name": "العربية",
        "language_code": "ar",
        
        # App info
        "app_name": "محمل تيليجرام",
        "app_version": "الإصدار 2.0",
        "created_by": "تم الإنشاء بواسطة Aviel.AI",
        "license": "رخصة MIT - مجاني ومفتوح المصدر",
        
        # Menu
        "menu_settings": "الإعدادات",
        "menu_language": "اللغة",
        "menu_about": "حول",
        "menu_help": "مساعدة",
        
        # Steps
        "step_setup": "الإعداد",
        "step_scan": "المسح",
        "step_select": "اختيار",
        "step_download": "التحميل",
        
        # Setup page
        "setup_title": "إعداد الاتصال بتيليجرام",
        "setup_instructions": """
        <div dir="rtl" style="text-align: center; font-family: Arial;">
        <p><b>انقر على الزر أدناه للحصول على بيانات اعتماد API</b></p>
        <p>سيُطلب منك تسجيل الدخول إلى تيليجرام والحصول على أرقام التعريف</p>
        </div>
        """,
        "btn_open_telegram": "🌐 افتح my.telegram.org",
        "label_api_id": "API ID:",
        "label_api_hash": "API Hash:",
        "label_phone": "الهاتف:",
        "placeholder_api_id": "12345678",
        "placeholder_api_hash": "a1b2c3d4...",
        "placeholder_phone": "+966501234567",
        "btn_save_continue": "حفظ ومتابعة ←",
        
        # Continue with Arabic translations...
        "scan_title": "مسح المجموعة/القناة",
        "select_title": "اختر الملفات للتحميل",
        "download_completed": "✓ اكتمل التحميل!",
        
        # ... (shortened for brevity)
    }
}


# Global translation instance
_translator: Optional[Translation] = None

def get_translator() -> Translation:
    """Get the global translator instance"""
    global _translator
    if _translator is None:
        _translator = Translation()
    return _translator

def tr(key: str, **kwargs) -> str:
    """Quick translation function"""
    return get_translator().get(key, **kwargs)
