<div align="center">

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/High%20Voltage.png" alt="⚡" width="80" height="80" />

# Telegram Downloader

### ULTIMATE PRO · v2.2.0

<p align="center">
  <img src="https://img.shields.io/badge/version-2.2.0_ULTIMATE_PRO-FFD700?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/status-stable-22C55E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/license-MIT-8B5CF6?style=for-the-badge" />
</p>

<p align="center">
  <b>The most powerful Telegram media downloader — parallel engine, dark mode, bilingual (EN/HE)</b>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-whats-new">What's New</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#%EF%B8%8F-configuration">Configuration</a> •
  <a href="#-license">License</a>
  &nbsp;|&nbsp;
  <a href="#hebrew">🇮🇱 עברית</a>
</p>

---

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### ⚡ Performance
- **Parallel Engine** — Download up to **3 files simultaneously**
- **Resume Mechanism** — Continue from where you stopped, no duplicate downloads
- **Real-time Stats** — Live speed (KB/s) + ETA display
- **Semaphore Control** — Proper API & resource management

</td>
<td width="50%">

### 🎨 Interface
- **Dark Mode** — Full dark theme, easy on the eyes
- **Smart Search** — Instant file-name filtering within scan results
- **Advanced Filters** — Combine type + keyword filters simultaneously
- **Desktop Notifications** — System alert when download completes

</td>
</tr>
<tr>
<td width="50%">

### 🔒 Security & Privacy
- **Local-only storage** — No cloud, no tracking, no telemetry
- **2FA Support** — Full Two-Factor Authentication
- **Session handling** — Secure Telethon session management

</td>
<td width="50%">

### 🌍 Usability
- **Bilingual (EN / HE)** — Switch language at runtime
- **RTL Support** — Native Hebrew right-to-left layout
- **Material Design ULTIMATE** — Clean, modern UI
- **Restricted Channels** — Works with some restricted sources

</td>
</tr>
</table>

---

## 🚀 What's New in v2.2.0 ULTIMATE PRO

> This release is the pinnacle of the project — maximum performance, refined UX, and zero-regression stability.

| Category | Change |
|---|---|
| 🏎️ **Speed** | Parallel download engine — up to 3 concurrent downloads |
| 🔄 **Resume** | Interrupted downloads now continue from exact stop point |
| 📊 **Stats** | Real-time KB/s speed + ETA shown in UI |
| 🌙 **Dark Mode** | Full dark theme across all windows |
| 🔍 **Search** | Live search bar in scan results |
| 🎛️ **Filters** | Type filter + text search can be used simultaneously |
| 🔔 **Notifications** | Windows desktop notification on completion |
| 🌐 **i18n** | Hebrew ↔ English switch without restart |
| 🐛 **Bugfix** | Video selection & checkbox issues fully resolved |
| 🧱 **Stability** | Semaphore-based concurrency for safe API usage |

---

## ⚡ Quick Start

### Prerequisites

```
Python 3.10+   Windows 10/11   Telegram API credentials (api_id + api_hash)
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/aviel-ai/telegram-downloader.git
cd telegram-downloader

# 2. Install dependencies (Windows)
install.bat

# 3. Launch the app
run.bat
```

### Getting your Telegram API credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in → **API development tools**
3. Create a new application
4. Copy your `api_id` and `api_hash` into the app on first launch

---

## 🖥️ Usage

```
1. Launch → Enter your phone number + 2FA code (once)
2. Paste a Telegram group or channel link
3. Click "Scan" — files appear in the list
4. Use Search + Filters to find what you need
5. Select files (or Select All) → Download
6. Files saved to your chosen output folder
```

### Supported file types

| Type | Extensions |
|---|---|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.webp` `.gif` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` `.mov` `.webm` |
| 📄 Documents | `.pdf` `.docx` `.xlsx` `.pptx` `.txt` |
| 🗜️ Archives | `.zip` `.rar` `.7z` `.tar.gz` |

---

## ⚙️ Configuration

On first run, a `config.json` is created automatically. You can edit it manually:

```json
{
  "api_id": 123456,
  "api_hash": "your_api_hash_here",
  "download_path": "C:/Downloads/Telegram",
  "language": "he",
  "dark_mode": true,
  "parallel_workers": 3,
  "resume_enabled": true
}
```

| Key | Default | Description |
|---|---|---|
| `parallel_workers` | `3` | Max simultaneous downloads (1–5 recommended) |
| `language` | `"he"` | `"he"` for Hebrew, `"en"` for English |
| `dark_mode` | `true` | Enable/disable dark theme |
| `resume_enabled` | `true` | Continue interrupted downloads |

---

## 🏗️ Architecture

```
telegram-downloader/
├── main.py              # Entry point, UI bootstrap
├── downloader.py        # Parallel download engine (Semaphore)
├── scanner.py           # Channel/group media scanner
├── ui/
│   ├── main_window.py   # PyQt6 main window
│   ├── filter_bar.py    # Search + type filters
│   └── dark_theme.py    # Dark mode stylesheet
├── lang/
│   ├── he.json          # Hebrew strings
│   └── en.json          # English strings
├── install.bat          # Dependency installer
├── run.bat              # App launcher
└── config.json          # Auto-generated on first run
```

---

## 📦 Dependencies

```
telethon        # Telegram MTProto client
PyQt6           # GUI framework
asyncio         # Async I/O engine
aiofiles        # Async file writing
plyer           # Desktop notifications
```

---

## 🛡️ Privacy & Security

- ✅ All data stored **locally only** — no external servers
- ✅ Session files encrypted by Telethon
- ✅ No analytics, no telemetry, no network calls except Telegram API
- ✅ Open source — audit the code yourself

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

```bash
# Fork → Clone → Create branch → Make changes → PR
git checkout -b feature/your-feature-name
```

---

## 📜 License

```
MIT License
Copyright (c) 2026 Aviel.AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

<div align="center">

Made with ❤️ by **[Aviel.AI](https://aviel.ai)** · Israel 🇮🇱

⭐ Star this repo if it helped you!

</div>

---
---

<a name="hebrew"></a>

<div align="center">

# 🇮🇱 תיעוד בעברית

</div>

## ✨ תכונות עיקריות

<table dir="rtl">
<tr>
<td width="50%">

### ⚡ ביצועים
- **מנוע מקבילי** — הורדת עד **3 קבצים בו-זמנית**
- **מנגנון Resume** — המשך מנקודת עצירה, ללא הורדות כפולות
- **סטטיסטיקות אמת** — מהירות (KB/s) + ETA בזמן אמת
- **ניהול Semaphore** — שימוש בטוח במשאבי API

</td>
<td width="50%">

### 🎨 ממשק
- **מצב כהה** — ערכת נושא כהה מלאה
- **חיפוש חכם** — סינון לפי שם קובץ בתוצאות הסריקה
- **סינון מתקדם** — שילוב סוג + מילת חיפוש בו-זמנית
- **התראות מערכת** — הודעה למחשב בסיום ההורדה

</td>
</tr>
</table>

---

## 🚀 מה חדש בגרסה 2.2.0 ULTIMATE PRO

| קטגוריה | שינוי |
|---|---|
| 🏎️ **מהירות** | מנוע הורדה מקבילי — עד 3 הורדות בו-זמנית |
| 🔄 **Resume** | הורדות שנקטעו ממשיכות מנקודת העצירה המדויקת |
| 📊 **סטטיסטיקות** | מהירות KB/s וזמן משוער בממשק |
| 🌙 **מצב כהה** | ערכת נושא כהה לכל חלונות האפליקציה |
| 🔍 **חיפוש** | שורת חיפוש חיה בתוצאות הסריקה |
| 🎛️ **סינון** | סינון סוג + חיפוש טקסטואלי בו-זמנית |
| 🔔 **התראות** | התראת Windows בסיום הורדה |
| 🌐 **שפות** | עברית ↔ אנגלית ללא הפעלה מחדש |
| 🐛 **תיקון באגים** | בעיות בחירת וידאו ותיבות סימון — נפתרו לחלוטין |
| 🧱 **יציבות** | Semaphore לניהול מקבילי בטוח |

---

## ⚡ התחלה מהירה

### דרישות מקדימות

```
Python 3.10+   Windows 10/11   פרטי API של Telegram (api_id + api_hash)
```

### התקנה

```bash
# 1. שכפל את הריפו
git clone https://github.com/aviel-ai/telegram-downloader.git
cd telegram-downloader

# 2. התקן ספריות (Windows)
install.bat

# 3. הפעל
run.bat
```

### קבלת פרטי API של Telegram

1. כנס ל-[my.telegram.org](https://my.telegram.org)
2. התחבר ← **API development tools**
3. צור אפליקציה חדשה
4. העתק `api_id` ו-`api_hash` לאפליקציה בהפעלה הראשונה

---

## 🖥️ שימוש

```
1. הפעל ← הזן מספר טלפון + קוד 2FA (פעם אחת)
2. הדבק לינק לקבוצה או ערוץ בטלגרם
3. לחץ "סרוק" — קבצים יופיעו ברשימה
4. השתמש בחיפוש + סינון למצוא מה שצריך
5. סמן קבצים (או "בחר הכל") ← הורד
6. קבצים נשמרים לתיקייה שבחרת
```

---

## ⚙️ הגדרות

בהפעלה ראשונה נוצר אוטומטית `config.json`. אפשר לערוך ידנית:

```json
{
  "api_id": 123456,
  "api_hash": "your_api_hash_here",
  "download_path": "C:/Downloads/Telegram",
  "language": "he",
  "dark_mode": true,
  "parallel_workers": 3,
  "resume_enabled": true
}
```

| מפתח | ברירת מחדל | תיאור |
|---|---|---|
| `parallel_workers` | `3` | מקסימום הורדות מקביליות (1–5 מומלץ) |
| `language` | `"he"` | `"he"` לעברית, `"en"` לאנגלית |
| `dark_mode` | `true` | הפעל/כבה מצב כהה |
| `resume_enabled` | `true` | המשך הורדות שנקטעו |

---

## 🛡️ פרטיות ואבטחה

- ✅ כל המידע נשמר **מקומית בלבד** — אין שרתים חיצוניים
- ✅ קבצי Session מוצפנים על ידי Telethon
- ✅ ללא ניתוח נתונים, ללא טלמטריה
- ✅ קוד פתוח — אפשר לבדוק בעצמך

---

## 📜 רישיון

```
MIT License — חופשי לשימוש ושינוי
Copyright (c) 2026 Aviel.AI
```

---

<div align="center">

נוצר באהבה על ידי **[Aviel.AI](https://aviel.ai)** · ישראל 🇮🇱

⭐ תן כוכב אם הכלי עזר לך!

</div>
