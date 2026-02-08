# ❓ Frequently Asked Questions (FAQ) for Telegram Downloader

This section addresses common questions about Telegram Downloader. If you don't find your answer here, please refer to the [Troubleshooting Guide](TROUBLESHOOTING.md) or open an issue on our [GitHub Issues page](https://github.com/Avielzi/telegram-downloader/issues).

## General Questions

### Q: What is Telegram Downloader?

A: Telegram Downloader is a desktop application designed to help users efficiently download media (photos, videos, documents, etc.) from Telegram channels and groups. It features a modern graphical user interface and advanced filtering options.

### Q: Is Telegram Downloader free?

A: Yes, Telegram Downloader is completely free and open-source, licensed under the MIT License.

### Q: What operating systems does it support?

A: It primarily supports Windows 10/11. With manual installation from source, it can also run on Linux and macOS.

### Q: Is it safe to use?

A: Yes, Telegram Downloader connects directly to the official Telegram API. All your data and downloaded files remain on your local machine. It does not collect any telemetry or personal information.

### Q: Does it support 2FA (Two-Factor Authentication)?

A: Yes, it fully supports Telegram's two-factor authentication for enhanced account security.

## Technical Questions

### Q: What Python version is required?

A: Telegram Downloader requires Python 3.8 or newer.

### Q: What are the main dependencies?

A: The main dependencies are PyQt6 for the user interface and Telethon for interacting with the Telegram API.

### Q: How do I update the application?

A: To update, you can usually pull the latest changes from the GitHub repository (`git pull origin main`) and then reinstall dependencies (`pip install -r requirements.txt --upgrade`). For Windows users, a `repair.bat` script might be available for easier updates.

### Q: Can I download from private channels/groups?

A: Yes, if you are a member of the private channel/group and have correctly configured your API credentials, you can download media from them.

### Q: Why are some files not downloading?

A: This could be due to several reasons:
-   Insufficient disk space.
-   Lack of write permissions in the destination folder.
-   Unstable internet connection.
-   The file might have been deleted from Telegram or is no longer accessible.

Refer to the [Troubleshooting Guide](TROUBLESHOOTING.md) for more details.

## Contribution Questions

### Q: How can I contribute to the project?

A: We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on reporting bugs, suggesting features, and submitting code.

### Q: Can I help with translations?

A: Absolutely! We appreciate help with translations. Please refer to the `i18n.py` file in the project and submit your changes via a Pull Request. New languages are always welcome.

---

## 🇮🇱 שאלות נפוצות (FAQ) עבור Telegram Downloader

סעיף זה עונה על שאלות נפוצות לגבי Telegram Downloader. אם אינכם מוצאים את התשובה כאן, אנא עיינו ב[מדריך פתרון בעיות](TROUBLESHOOTING.md) או פתחו גיליון בדף [GitHub Issues](https://github.com/Avielzi/telegram-downloader/issues) שלנו.

## שאלות כלליות

### ש: מהו Telegram Downloader?

ת: Telegram Downloader הוא יישום שולחני שנועד לעזור למשתמשים להוריד ביעילות מדיה (תמונות, סרטונים, מסמכים וכו') מערוצים וקבוצות בטלגרם. הוא כולל ממשק משתמש גרפי מודרני ואפשרויות סינון מתקדמות.

### ש: האם Telegram Downloader חינמי?

ת: כן, Telegram Downloader חינמי לחלוטין וקוד פתוח, ברישיון MIT.

### ש: אילו מערכות הפעלה הוא תומך?

ת: הוא תומך בעיקר ב-Windows 10/11. עם התקנה ידנית מקוד המקור, הוא יכול לרוץ גם על לינוקס ו-macOS.

### ש: האם זה בטוח לשימוש?

ת: כן, Telegram Downloader מתחבר ישירות ל-API הרשמי של טלגרם. כל הנתונים והקבצים שהורדתם נשארים במחשב המקומי שלכם. הוא אינו אוסף כל טלמטריה או מידע אישי.

### ש: האם הוא תומך ב-2FA (אימות דו-שלבי)?

ת: כן, הוא תומך באופן מלא באימות דו-שלבי של טלגרם לאבטחת חשבון משופרת.

## שאלות טכניות

### ש: איזו גרסת פייתון נדרשת?

ת: Telegram Downloader דורש פייתון 3.8 ומעלה.

### ש: מהן התלויות העיקריות?

ת: התלויות העיקריות הן PyQt6 עבור ממשק המשתמש ו-Telethon לאינטראקציה עם ה-API של טלגרם.

### ש: איך אני מעדכן את היישום?

ת: כדי לעדכן, בדרך כלל ניתן למשוך את השינויים האחרונים מריפוזיטורי ה-GitHub (`git pull origin main`) ולאחר מכן להתקין מחדש תלויות (`pip install -r requirements.txt --upgrade`). למשתמשי Windows, ייתכן שסקריפט `repair.bat` זמין לעדכונים קלים יותר.

### ש: האם ניתן להוריד מערוצים/קבוצות פרטיים?

ת: כן, אם אתם חברים בערוץ/קבוצה הפרטיים והגדרתם נכון את פרטי ה-API שלכם, תוכלו להוריד מהם מדיה.

### ש: מדוע קבצים מסוימים אינם יורדים?

ת: זה יכול לנבוע ממספר סיבות:
-   שטח דיסק לא מספיק.
-   חוסר הרשאות כתיבה בתיקיית היעד.
-   חיבור אינטרנט לא יציב.
-   הקובץ אולי נמחק מטלגרם או אינו נגיש יותר.

עיינו ב[מדריך פתרון בעיות](TROUBLESHOOTING.md) לפרטים נוספים.

## שאלות תרומה

### ש: איך אני יכול לתרום לפרויקט?

ת: אנו מברכים על תרומות! אנא עיינו בקובץ [CONTRIBUTING.md](CONTRIBUTING.md) שלנו להנחיות על דיווח באגים, הצעת תכונות ושליחת קוד.

### ש: האם אני יכול לעזור בתרגומים?

ת: בהחלט! אנו מעריכים עזרה בתרגומים. אנא עיינו בקובץ `i18n.py` בפרויקט ושלחו את השינויים שלכם באמצעות בקשת משיכה. שפות חדשות תמיד יתקבלו בברכה.
