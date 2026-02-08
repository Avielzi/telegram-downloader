# 🚀 Usage Guide for Telegram Downloader

This guide will walk you through the process of using Telegram Downloader to efficiently download media from Telegram channels and groups.

## Prerequisites

Before proceeding, ensure you have successfully installed Telegram Downloader and configured your Telegram API credentials as described in the [Installation Guide](INSTALLATION.md) and [API Setup Guide](API_SETUP.md).

## Step 1: Launch the Application

Start Telegram Downloader using one of the methods described in the [Installation Guide](INSTALLATION.md):

-   **Windows**: Double-click `run.bat`.
-   **Cross-platform**: Run `python telegram_downloader.py` in your terminal.

## Step 2: Scan for Media

1.  **Enter Channel/Group Link**: In the application's main interface, locate the input field for the Telegram channel or group link. You can enter either a full URL (e.g., `https://t.me/groupname`) or a username (e.g., `@groupname`).
2.  **Specify Message Limit**: Choose the number of messages you wish to scan. This can range from 10 to 10,000. A higher number will scan more history but may take longer.
3.  **Start Scanning**: Click the "Start Scan" (🔍) button. The application will connect to Telegram and begin fetching media information. A progress bar will indicate the scanning status.

## Step 3: Select and Filter Files

Once the scan is complete, a list of available media files will be displayed.

1.  **Review Files**: Browse through the list of files. Each entry will typically show the file name, type, size, and sender.
2.  **Apply Filters (Optional)**: Use the filter options (e.g., Photos, Videos, Documents, Archives) to narrow down the list and find specific types of media.
3.  **Select Files**: Use the checkboxes next to each file to select the ones you want to download. You can also use multi-selection features (e.g., Shift + Click) for convenience.
4.  **Choose Destination Folder**: Click the "Browse" button to select a local folder where the downloaded files will be saved.

## Step 4: Download Media

1.  **Start Download**: After selecting your files and destination, click the "Download Selected Files" (⬇) button.
2.  **Monitor Progress**: The application will display a real-time progress bar for each file being downloaded, as well as an overall progress indicator.
3.  **Completion**: Once all selected files are downloaded, a notification will appear, and the files will be available in your chosen destination folder.

## Tips for Efficient Usage

-   **Start Small**: For your first few downloads, try scanning and downloading a smaller number of messages (e.g., 100) to familiarize yourself with the process.
-   **Utilize Filters**: Filters can significantly speed up the process of finding specific media types in large channels.
-   **Organize Downloads**: Consider creating separate folders for different channels or media types to keep your downloads organized.
-   **Respect Copyrights**: Only download media that you have permission to access and use.

---

## 🇮🇱 מדריך שימוש עבור Telegram Downloader

מדריך זה ילווה אתכם בתהליך השימוש ב-Telegram Downloader להורדת מדיה יעילה מערוצים וקבוצות בטלגרם.

## דרישות קדם

לפני שתמשיכו, ודאו שהתקנתם בהצלחה את Telegram Downloader והגדרתם את פרטי ה-API של טלגרם כמתואר ב[מדריך ההתקנה](INSTALLATION.md) וב[מדריך הגדרת API](API_SETUP.md).

## שלב 1: הפעלת היישום

הפעילו את Telegram Downloader באמצעות אחת מהשיטות המתוארות ב[מדריך ההתקנה](INSTALLATION.md):

-   **Windows**: לחצו לחיצה כפולה על `run.bat`.
-   **קרוס-פלטפורמה**: הריצו `python telegram_downloader.py` בטרמינל שלכם.

## שלב 2: סריקת מדיה

1.  **הזינו קישור לערוץ/קבוצה**: בממשק הראשי של היישום, אתרו את שדה הקלט עבור קישור לערוץ או קבוצת טלגרם. ניתן להזין כתובת URL מלאה (לדוגמה, `https://t.me/groupname`) או שם משתמש (לדוגמה, `@groupname`).
2.  **ציינו מגבלת הודעות**: בחרו את מספר ההודעות שברצונכם לסרוק. טווח המספרים הוא בין 10 ל-10,000. מספר גבוה יותר יסרוק יותר היסטוריה אך עשוי לקחת זמן רב יותר.
3.  **התחילו בסריקה**: לחצו על כפתור "התחל סריקה" (🔍). היישום יתחבר לטלגרם ויתחיל לאחזר מידע על מדיה. סרגל התקדמות יציין את מצב הסריקה.

## שלב 3: בחירה וסינון קבצים

לאחר השלמת הסריקה, תוצג רשימה של קבצי המדיה הזמינים.

1.  **סקירת קבצים**: עברו על רשימת הקבצים. כל פריט יציג בדרך כלל את שם הקובץ, סוגו, גודלו והשולח.
2.  **החלת מסננים (אופציונלי)**: השתמשו באפשרויות הסינון (לדוגמה, תמונות, סרטונים, מסמכים, ארכיונים) כדי לצמצם את הרשימה ולמצוא סוגי מדיה ספציפיים.
3.  **בחירת קבצים**: השתמשו בתיבות הסימון שליד כל קובץ כדי לבחור את אלה שברצונכם להוריד. ניתן גם להשתמש בתכונות בחירה מרובה (לדוגמה, Shift + Click) לנוחות.
4.  **בחירת תיקיית יעד**: לחצו על כפתור "עיון" כדי לבחור תיקייה מקומית שבה יישמרו הקבצים שהורדו.

## שלב 4: הורדת מדיה

1.  **התחלת הורדה**: לאחר בחירת הקבצים והיעד שלכם, לחצו על כפתור "הורד קבצים נבחרים" (⬇).
2.  **מעקב אחר התקדמות**: היישום יציג סרגל התקדמות בזמן אמת עבור כל קובץ המורד, כמו גם מחוון התקדמות כולל.
3.  **השלמה**: לאחר שכל הקבצים שנבחרו יורדו, תופיע הודעה, והקבצים יהיו זמינים בתיקיית היעד שבחרתם.

## טיפים לשימוש יעיל

-   **התחילו בקטן**: עבור ההורדות הראשונות שלכם, נסו לסרוק ולהוריד מספר קטן יותר של הודעות (לדוגמה, 100) כדי להכיר את התהליך.
-   **נצלו מסננים**: מסננים יכולים להאיץ משמעותית את תהליך מציאת סוגי מדיה ספציפיים בערוצים גדולים.
-   **ארגנו הורדות**: שקלו ליצור תיקיות נפרדות עבור ערוצים או סוגי מדיה שונים כדי לשמור על סדר בהורדות שלכם.
-   **כבדו זכויות יוצרים**: הורידו רק מדיה שיש לכם הרשאה לגשת אליה ולהשתמש בה.
