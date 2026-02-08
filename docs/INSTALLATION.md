# 📦 Installation Guide for Telegram Downloader

This guide provides detailed instructions on how to install and set up Telegram Downloader on your system.

## Prerequisites

Before you begin, ensure you have the following:

-   **Operating System**: Windows 10/11 (primary support), Linux, or macOS.
-   **Python**: Version 3.8 or newer. You can download it from [python.org](https://www.python.org/).
    -   **Important**: During Python installation, make sure to check the option "Add Python to PATH".
-   **Internet Connection**: Required for downloading dependencies and connecting to Telegram API.

## Step-by-Step Installation

Follow these steps to get Telegram Downloader up and running:

### 1. Clone the Repository

Open your terminal or command prompt and clone the project repository:

```bash
git clone https://github.com/Avielzi/telegram-downloader.git
cd telegram-downloader
```

### 2. Install Dependencies

Telegram Downloader relies on several Python libraries. You can install them using one of the following methods:

#### Option A: Automatic Installation (Recommended for Windows)

For Windows users, simply double-click the `install.bat` file located in the project root directory. This script will automatically install all required Python packages.

```
install.bat
```

#### Option B: Manual Installation (Cross-platform)

If you are on Linux, macOS, or prefer a manual approach, you can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Once all dependencies are installed, you can launch Telegram Downloader:

#### Option A: Automatic Run (Recommended for Windows)

For Windows users, double-click the `run.bat` file in the project root directory. This will start the application.

```
run.bat
```

#### Option B: Manual Run (Cross-platform)

Alternatively, you can run the main Python script directly from your terminal:

```bash
python telegram_downloader.py
```

## Post-Installation

After successfully installing and running the application for the first time, you will need to configure your Telegram API credentials. Please refer to the [API Setup Guide](API_SETUP.md) for detailed instructions.

---

## 🇮🇱 מדריך התקנה עבור Telegram Downloader

מדריך זה מספק הוראות מפורטות כיצד להתקין ולהגדיר את Telegram Downloader במערכת שלכם.

## דרישות קדם

לפני שתתחילו, ודאו שיש לכם את הדברים הבאים:

-   **מערכת הפעלה**: Windows 10/11 (תמיכה עיקרית), לינוקס, או macOS.
-   **פייתון**: גרסה 3.8 ומעלה. ניתן להוריד אותה מ-[python.org](https://www.python.org/).
    -   **חשוב**: במהלך התקנת פייתון, ודאו לסמן את האפשרות "Add Python to PATH".
-   **חיבור לאינטרנט**: נדרש להורדת תלויות והתחברות ל-API של טלגרם.

## התקנה שלב אחר שלב

בצעו את השלבים הבאים כדי להפעיל את Telegram Downloader:

### 1. שכפול הריפוזיטורי

פתחו את הטרמינל או שורת הפקודה ושכפלו את ריפוזיטורי הפרויקט:

```bash
git clone https://github.com/Avielzi/telegram-downloader.git
cd telegram-downloader
```

### 2. התקנת תלויות

Telegram Downloader מסתמך על מספר ספריות פייתון. ניתן להתקין אותן באמצעות אחת מהשיטות הבאות:

#### אפשרות א​: התקנה אוטומטית (מומלץ עבור Windows)

למשתמשי Windows, פשוט לחצו לחיצה כפולה על הקובץ `install.bat` הנמצא בספריית השורש של הפרויקט. סקריפט זה יתקין אוטומטית את כל חבילות הפייתון הנדרשות.

```
install.bat
```

#### אפשרות ב​: התקנה ידנית (קרוס-פלטפורמה)

אם אתם משתמשים בלינוקס, macOS, או מעדיפים גישה ידנית, תוכלו להתקין את התלויות באמצעות `pip`:

```bash
pip install -r requirements.txt
```

### 3. הפעלת היישום

לאחר שכל התלויות הותקנו, תוכלו להפעיל את Telegram Downloader:

#### אפשרות א​: הפעלה אוטומטית (מומלץ עבור Windows)

למשתמשי Windows, לחצו לחיצה כפולה על הקובץ `run.bat` בספריית השורש של הפרויקט. פעולה זו תפעיל את היישום.

```
run.bat
```

#### אפשרות ב​: הפעלה ידנית (קרוס-פלטפורמה)

לחלופין, תוכלו להפעיל את סקריפט הפייתון הראשי ישירות מהטרמינל שלכם:

```bash
python telegram_downloader.py
```

## לאחר ההתקנה

לאחר התקנה והפעלה מוצלחת של היישום בפעם הראשונה, תצטרכו להגדיר את פרטי ה-API של טלגרם שלכם. אנא עיינו ב[מדריך הגדרת API](API_SETUP.md) להוראות מפורטות.
