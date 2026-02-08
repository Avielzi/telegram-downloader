# 📥 Telegram Downloader

[English](#english) | [עברית](#hebrew)

---

<div align="center">

![Version](https://img.shields.io/badge/version-2.1.1-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/status-stable-success)

**Modern media downloader for Telegram groups and channels**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

<a name="english"></a>
## 🇬🇧 English

**Telegram Downloader** is a powerful and professional tool designed for efficient bulk media downloading from Telegram channels and groups. Built with **PyQt6** for a modern graphical user interface and **Telethon** for robust Telegram API interaction, it offers a stable, user-friendly, and feature-rich experience for managing your Telegram media.

### 🌟 Features

- 📥 **Bulk Download**: Effortlessly download hundreds of files from any Telegram chat with a single click.
- 🔍 **Smart Scanning**: Automatically detect and list all available media within a specified group or channel.
- ✅ **Visual Selection**: Intuitive interface with checkboxes allows you to select precisely which files you want to download.
- 🎯 **Advanced Filtering**: Filter media by type, including photos, videos, documents, and archives, to quickly find what you need.
- 🌍 **Multi-language Support**: Comprehensive support for 5 languages: English, Hebrew, Spanish, Russian, and Arabic.
- 🎨 **Modern UI**: A sleek Material Design interface ensures a pleasant and efficient user experience, complete with real-time progress bars.
- 🔒 **Secure & Private**: Connects directly to the official Telegram API, ensuring your data remains local to your machine with no telemetry or tracking.
- 🔐 **2FA Support**: Full support for two-factor authentication for enhanced account security.
- ⚡ **Optimized Performance**: Features an entirely fixed AsyncIO event loop, leading to improved stability and faster download speeds.

### 📸 Screenshots & Demo

*(To be added: Please replace this section with actual screenshots or a GIF demonstrating the application's UI and functionality. For example, show the main window, scanning process, filtering options, and download progress.)*

### 📦 Installation

To get started with Telegram Downloader, follow these steps:

1.  **Install Python**: Ensure you have Python 3.8 or newer installed on your system. During installation, make sure to check the option 
to "Add Python to PATH". You can download Python from [python.org](https://www.python.org/).

2.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Avielzi/telegram-downloader.git
    cd telegram-downloader
    ```

3.  **Install Dependencies**:
    -   **Recommended (Windows)**: Double-click `install.bat`.
    -   **Manual (Cross-platform)**: Run `pip install -r requirements.txt` in your terminal.

4.  **Run the Application**:
    -   **Recommended (Windows)**: Double-click `run.bat`.
    -   **Manual (Cross-platform)**: Run `python telegram_downloader.py` in your terminal.

### 🚀 Quick Start Guide

1.  **API Setup (First Time Only)**:
    -   Open the application.
    -   Click "Open my.telegram.org" and log in with your phone number.
    -   Create a new application with "App title: `My Downloader`" and "Platform: `Desktop`".
    -   Copy your **API ID** and **API Hash**.
    -   Enter these credentials, along with your phone number, into the application and save.

2.  **Scan for Media**:
    -   Paste the link to a Telegram group or channel (e.g., `https://t.me/groupname` or `@groupname`).
    -   Specify the number of messages to scan (e.g., 10-10,000).
    -   Click "Start Scan" and wait for the process to complete.

3.  **Select and Filter**:
    -   Review the list of found files.
    -   Use the advanced filters to narrow down by type (photos, videos, etc.).
    -   Select the desired files using the checkboxes.
    -   Choose a destination folder for your downloads.

4.  **Download**: Click "Download Selected Files" and monitor the real-time progress. Once complete, your files will be in the chosen folder!

---

### 📖 Full Documentation

For more detailed information on installation, usage, API setup, troubleshooting, and frequently asked questions, please refer to the `docs/` folder:

-   [INSTALLATION.md](docs/INSTALLATION.md)
-   [USAGE.md](docs/USAGE.md)
-   [API_SETUP.md](docs/API_SETUP.md)
-   [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
-   [FAQ.md](docs/FAQ.md)

---

### 🤝 Contributing

We welcome contributions from the community! If you'd like to contribute, please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to report bugs, suggest features, and submit pull requests.

---

### 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🙏 Credits

Created with ❤️ by **[Aviel.AI](https://github.com/avielai)**.

Built with:
-   [Python](https://www.python.org/)
-   [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
-   [Telethon](https://github.com/LonamiWebs/Telethon)
-   [cryptg](https://github.com/eternnoir/cryptg)

---

### ⭐ Show your support

Give a ⭐ if this project helped you!

---

<a name="hebrew"></a>
## 🇮🇱 עברית

**Telegram Downloader** הוא כלי עוצמתי ומקצועי המיועד להורדה המונית ויעילה של מדיה מערוצים וקבוצות בטלגרם. נבנה באמצעות **PyQt6** לממשק משתמש גרפי מודרני ו-**Telethon** לאינטראקציה חזקה עם ה-API של טלגרם, הוא מציע חוויה יציבה, ידידותית למשתמש ועשירה בתכונות לניהול המדיה שלכם מטלגרם.

### 🌟 תכונות עיקריות

- 📥 **הורדה המונית**: הורידו בקלות מאות קבצים מכל צ'אט בטלגרם בלחיצה אחת.
- 🔍 **סריקה חכמה**: זיהוי אוטומטי והצגת כל המדיה הזמינה בתוך קבוצה או ערוץ נבחרים.
- ✅ **בחירה ויזואלית**: ממשק אינטואיטיבי עם תיבות סימון מאפשר לכם לבחור בדיוק אילו קבצים ברצונכם להוריד.
- 🎯 **סינון מתקדם**: סננו מדיה לפי סוג, כולל תמונות, סרטונים, מסמכים וארכיונים, כדי למצוא במהירות את מה שאתם צריכים.
- 🌍 **תמיכה רב-לשונית**: תמיכה מקיפה ב-5 שפות: אנגלית, עברית, ספרדית, רוסית וערבית.
- 🎨 **ממשק מודרני**: ממשק Material Design אלגנטי מבטיח חווית משתמש נעימה ויעילה, עם סרגלי התקדמות בזמן אמת.
- 🔒 **מאובטח ופרטי**: מתחבר ישירות ל-API הרשמי של טלגרם, ומבטיח שהנתונים שלכם יישארו מקומיים למחשב שלכם ללא טלמטריה או מעקב.
- 🔐 **תמיכה ב-2FA**: תמיכה מלאה באימות דו-שלבי לאבטחת חשבון משופרת.
- ⚡ **ביצועים אופטימליים**: כולל תיקון מלא של לולאת האירועים AsyncIO, מה שמוביל ליציבות משופרת ומהירויות הורדה מהירות יותר.

### 📸 צילומי מסך והדגמה

*(יוסף בהמשך: אנא החליפו סעיף זה בצילומי מסך או GIF המדגימים את ממשק המשתמש והפונקציונליות של היישום. לדוגמה, הציגו את החלון הראשי, תהליך הסריקה, אפשרויות הסינון והתקדמות ההורדה.)*

### 📦 התקנה

כדי להתחיל להשתמש ב-Telegram Downloader, בצעו את השלבים הבאים:

1.  **התקינו Python**: ודאו שמותקן לכם Python 3.8 ומעלה במערכת. במהלך ההתקנה, ודאו לסמן את האפשרות "Add Python to PATH". ניתן להוריד Python מ-[python.org](https://www.python.org/).

2.  **שכפלו את הריפוזיטורי**:
    ```bash
    git clone https://github.com/Avielzi/telegram-downloader.git
    cd telegram-downloader
    ```

3.  **התקינו תלויות**:
    -   **מומלץ (Windows)**: לחצו לחיצה כפולה על `install.bat`.
    -   **ידני (קרוס-פלטפורמה)**: הריצו `pip install -r requirements.txt` בטרמינל שלכם.

4.  **הפעילו את היישום**:
    -   **מומלץ (Windows)**: לחצו לחיצה כפולה על `run.bat`.
    -   **ידני (קרוס-פלטפורמה)**: הריצו `python telegram_downloader.py` בטרמינל שלכם.

### 🚀 מדריך התחלה מהירה

1.  **הגדרת API (פעם ראשונה בלבד)**:
    -   פתחו את היישום.
    -   לחצו "Open my.telegram.org" והתחברו עם מספר הטלפון שלכם.
    -   צרו יישום חדש עם "App title: `My Downloader`" ו-"Platform: `Desktop`".
    -   העתיקו את **API ID** ו-**API Hash** שלכם.
    -   הזינו את הפרטים הללו, יחד עם מספר הטלפון שלכם, ליישום ושמרו.

2.  **סריקת מדיה**:
    -   הדביקו קישור לקבוצת או ערוץ טלגרם (לדוגמה, `https://t.me/groupname` או `@groupname`).
    -   ציינו את מספר ההודעות לסריקה (לדוגמה, 10-10,000).
    -   לחצו "התחל סריקה" והמתינו לסיום התהליך.

3.  **בחירה וסינון**:
    -   עברו על רשימת הקבצים שנמצאו.
    -   השתמשו במסננים המתקדמים כדי לצמצם לפי סוג (תמונות, סרטונים וכו').
    -   בחרו את הקבצים הרצויים באמצעות תיבות הסימון.
    -   בחרו תיקיית יעד להורדות שלכם.

4.  **הורדה**: לחצו "הורד קבצים נבחרים" ועקבו אחר ההתקדמות בזמן אמת. לאחר השלמת ההורדה, הקבצים שלכם יהיו בתיקייה שנבחרה!

---

### 📖 תיעוד מלא

למידע מפורט יותר על התקנה, שימוש, הגדרת API, פתרון בעיות ושאלות נפוצות, אנא עיינו בתיקיית `docs/`:

-   [INSTALLATION.md](docs/INSTALLATION.md)
-   [USAGE.md](docs/USAGE.md)
-   [API_SETUP.md](docs/API_SETUP.md)
-   [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
-   [FAQ.md](docs/FAQ.md)

---

### 🤝 תרומה לפרויקט

אנו מברכים על תרומות מהקהילה! אם תרצו לתרום, אנא קראו את המדריך [CONTRIBUTING.md](CONTRIBUTING.md) לפרטים על אופן דיווח באגים, הצעת תכונות ושליחת בקשות משיכה (Pull Requests).

---

### 📜 רישיון

פרויקט זה מופץ תחת רישיון MIT - ראו קובץ [LICENSE](LICENSE) לפרטים נוספים.

---

### 🙏 קרדיטים

נוצר באהבה על ידי **[Aviel.AI](https://github.com/avielai)**.

נבנה עם:
-   [Python](https://www.python.org/)
-   [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
-   [Telethon](https://github.com/LonamiWebs/Telethon)
-   [cryptg](https://github.com/eternnoir/cryptg)

---

### ⭐ הראו את תמיכתכם

תנו ⭐ אם פרויקט זה עזר לכם!

---

<div align="center">

**תודה שהשתמשת ב-Telegram Downloader!**

**נוצר באהבה על ידי [Aviel.AI](https://github.com/avielai)** ❤️

[⬆ חזרה למעלה](#-telegram-downloader)

</div>

<!-- Updated author configuration -->
