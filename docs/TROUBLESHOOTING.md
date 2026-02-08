# 🛠️ Troubleshooting Guide for Telegram Downloader

This guide provides solutions to common issues you might encounter while using Telegram Downloader. If your problem is not listed here, please refer to the [FAQ](FAQ.md) or open an issue on our [GitHub Issues page](https://github.com/Avielzi/telegram-downloader/issues).

## Common Issues and Solutions

### Issue: "Python is not installed" or "Python command not found"

**Solution:**
1.  **Install Python**: Download and install Python 3.8+ from [python.org](https://www.python.org/).
2.  **Add to PATH**: During installation, ensure you check the option "Add Python to PATH". If you missed this, you might need to reinstall Python or manually add it to your system's PATH environment variable.

### Issue: "Telethon is not installed" or missing dependencies

**Solution:**
1.  **Run `install.bat`**: If you are on Windows, double-click the `install.bat` file in the project root directory. This script will automatically install all required Python packages.
2.  **Manual Installation**: Open your terminal or command prompt, navigate to the `telegram-downloader` directory, and run: `pip install -r requirements.txt`.

### Issue: "AsyncIO event loop" errors

**Solution:**
This version (v2.1.1) has significantly improved AsyncIO handling. If you still encounter this error:
1.  **Repair Installation**: Double-click `repair.bat` (Windows) or run `pip install -r requirements.txt --upgrade` (cross-platform) to reinstall all dependencies.
2.  **Restart Application**: Close and restart Telegram Downloader.

### Issue: "Can't connect to group/channel" or "Authorization failed"

**Solution:**
1.  **Verify Link**: Ensure the Telegram group/channel link or username is correct and accessible.
2.  **Internet Connection**: Check your internet connection for stability.
3.  **API Credentials**: Double-check your API ID, API Hash, and phone number in the application settings. Refer to the [API Setup Guide](API_SETUP.md).
4.  **Telegram Account Status**: Make sure your Telegram account is not restricted or banned.
5.  **Try Again**: Sometimes, temporary network issues can cause this. Wait a few minutes and try again.

### Issue: "Download fails" or files are corrupted

**Solution:**
1.  **Disk Space**: Verify that you have sufficient free disk space on your chosen download drive.
2.  **Folder Permissions**: Ensure Telegram Downloader has the necessary write permissions for the selected destination folder. Try choosing a different folder (e.g., your Desktop or Downloads folder).
3.  **Internet Stability**: Unstable internet connection during download can lead to corrupted files. Ensure a stable connection.

### Issue: Application UI is not responsive or freezes

**Solution:**
1.  **Restart Application**: Close and restart Telegram Downloader.
2.  **Update Dependencies**: Ensure all Python dependencies are up to date by running `pip install -r requirements.txt --upgrade`.
3.  **System Resources**: Check if your system has enough RAM and CPU resources. Close other demanding applications if necessary.

## Getting Further Help

If you've tried the solutions above and are still experiencing issues, please:

-   Consult the [FAQ](FAQ.md) for more general questions.
-   Open a new issue on our [GitHub Issues page](https://github.com/Avielzi/telegram-downloader/issues). Provide as much detail as possible about your problem, including steps to reproduce, error messages, and your system configuration.

---

## 🇮🇱 מדריך פתרון בעיות עבור Telegram Downloader

מדריך זה מספק פתרונות לבעיות נפוצות שעלולות להיתקל בהן בעת השימוש ב-Telegram Downloader. אם הבעיה שלכם אינה מופיעה כאן, אנא עיינו ב[שאלות נפוצות](FAQ.md) או פתחו גיליון בדף [GitHub Issues](https://github.com/Avielzi/telegram-downloader/issues) שלנו.

## בעיות נפוצות ופתרונות

### בעיה: "Python אינו מותקן" או "פקודת Python לא נמצאה"

**פתרון:**
1.  **התקינו Python**: הורידו והתקינו Python 3.8+ מ-[python.org](https://www.python.org/).
2.  **הוסיפו ל-PATH**: במהלך ההתקנה, ודאו שסימנתם את האפשרות "Add Python to PATH". אם פספסתם זאת, ייתכן שתצטרכו להתקין מחדש את Python או להוסיף אותו ידנית למשתנה הסביבה PATH של המערכת שלכם.

### בעיה: "Telethon אינו מותקן" או תלויות חסרות

**פתרון:**
1.  **הריצו `install.bat`**: אם אתם משתמשים ב-Windows, לחצו לחיצה כפולה על הקובץ `install.bat` בספריית השורש של הפרויקט. סקריפט זה יתקין אוטומטית את כל חבילות הפייתון הנדרשות.
2.  **התקנה ידנית**: פתחו את הטרמינל או שורת הפקודה שלכם, נווטו לספריית `telegram-downloader`, והריצו: `pip install -r requirements.txt`.

### בעיה: שגיאות "AsyncIO event loop"

**פתרון:**
גרסה זו (v2.1.1) שיפרה משמעותית את הטיפול ב-AsyncIO. אם אתם עדיין נתקלים בשגיאה זו:
1.  **תיקון התקנה**: לחצו לחיצה כפולה על `repair.bat` (Windows) או הריצו `pip install -r requirements.txt --upgrade` (קרוס-פלטפורמה) כדי להתקין מחדש את כל התלויות.
2.  **הפעלה מחדש של היישום**: סגרו והפעילו מחדש את Telegram Downloader.

### בעיה: "לא ניתן להתחבר לקבוצה/ערוץ" או "כשל באימות"

**פתרון:**
1.  **אמתו קישור**: ודאו שקישור או שם המשתמש של קבוצת/ערוץ הטלגרם נכונים ונגישים.
2.  **חיבור לאינטרנט**: בדקו את יציבות חיבור האינטרנט שלכם.
3.  **פרטי API**: בדקו שוב את ה-API ID, ה-API Hash ומספר הטלפון שלכם בהגדרות היישום. עיינו ב[מדריך הגדרת API](API_SETUP.md).
4.  **סטטוס חשבון טלגרם**: ודאו שחשבון הטלגרם שלכם אינו מוגבל או חסום.
5.  **נסו שוב**: לעיתים, בעיות רשת זמניות עלולות לגרום לכך. המתינו מספר דקות ונסו שוב.

### בעיה: "ההורדה נכשלת" או קבצים פגומים

**פתרון:**
1.  **שטח דיסק**: ודאו שיש לכם מספיק מקום פנוי בכונן ההורדות שבחרתם.
2.  **הרשאות תיקייה**: ודאו של-Telegram Downloader יש את הרשאות הכתיבה הנדרשות לתיקיית היעד שנבחרה. נסו לבחור תיקייה אחרת (לדוגמה, שולחן העבודה או תיקיית ההורדות שלכם).
3.  **יציבות אינטרנט**: חיבור אינטרנט לא יציב במהלך ההורדה עלול להוביל לקבצים פגומים. ודאו חיבור יציב.

### בעיה: ממשק המשתמש של היישום אינו מגיב או קופא

**פתרון:**
1.  **הפעלה מחדש של היישום**: סגרו והפעילו מחדש את Telegram Downloader.
2.  **עדכון תלויות**: ודאו שכל תלויות הפייתון מעודכנות על ידי הרצת `pip install -r requirements.txt --upgrade`.
3.  **משאבי מערכת**: בדקו אם למערכת שלכם יש מספיק זיכרון RAM ומשאבי מעבד. סגרו יישומים תובעניים אחרים במידת הצורך.

## קבלת עזרה נוספת

אם ניסיתם את הפתרונות לעיל ועדיין נתקלים בבעיות, אנא:

-   עיינו ב[שאלות נפוצות](FAQ.md) לשאלות כלליות יותר.
-   פתחו גיליון חדש בדף [GitHub Issues](https://github.com/Avielzi/telegram-downloader/issues) שלנו. ספקו כמה שיותר פרטים על הבעיה שלכם, כולל שלבים לשחזור, הודעות שגיאה ותצורת המערכת שלכם.
