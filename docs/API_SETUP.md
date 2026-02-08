# 🔑 Telegram API Setup Guide

To use Telegram Downloader, you need to obtain your personal Telegram API ID and API Hash. These credentials allow the application to securely connect to your Telegram account and access channels/groups.

## Step-by-Step API Setup

Follow these instructions carefully to get your API credentials:

### 1. Visit My Telegram API Development Tools

Open your web browser and navigate to the official Telegram API development tools page: [my.telegram.org](https://my.telegram.org/).

### 2. Log In to Your Telegram Account

-   Enter your phone number associated with your Telegram account.
-   Click "Next".
-   You will receive a confirmation code via Telegram. Enter this code on the website.
-   Click "Sign In".

### 3. Create a New Application

Once logged in, you will see a section titled "API Development Tools".

-   Click on "Create new application".
-   Fill in the required fields:
    -   **App title**: Enter a descriptive name for your application, e.g., `Telegram Downloader App`.
    -   **Short name**: A short, unique name for your app (e.g., `tgdownloader`).
    -   **Platform**: Select `Desktop`.
    -   **Description**: (Optional) Provide a brief description.
-   Click "Create Application".

### 4. Retrieve Your API Credentials

After creating the application, you will be redirected to a page displaying your application details. Here you will find:

-   **App api_id**: This is your API ID.
-   **App api_hash**: This is your API Hash.

**Important**: Keep these credentials confidential. Do not share them with anyone or commit them to public repositories.

### 5. Enter Credentials into Telegram Downloader

-   Open the Telegram Downloader application.
-   Navigate to the settings or initial setup screen.
-   Enter your **API ID**, **API Hash**, and your **Telegram Phone Number** into the respective fields.
-   Click "Save" or "Connect" to establish the connection.

## Troubleshooting API Connection Issues

If you encounter issues connecting to the Telegram API:

-   **Double-check Credentials**: Ensure your API ID, API Hash, and phone number are entered correctly.
-   **Internet Connection**: Verify that you have a stable internet connection.
-   **Telegram Account Status**: Make sure your Telegram account is active and not restricted.
-   **Two-Factor Authentication (2FA)**: If you have 2FA enabled on your Telegram account, the application will prompt you for the password. Enter it when requested.

If problems persist, refer to the [Troubleshooting Guide](TROUBLESHOOTING.md) or report an issue on GitHub.

---

## 🇮🇱 מדריך הגדרת Telegram API

כדי להשתמש ב-Telegram Downloader, עליכם להשיג את ה-API ID וה-API Hash האישיים שלכם בטלגרם. פרטים אלו מאפשרים ליישום להתחבר בצורה מאובטחת לחשבון הטלגרם שלכם ולגשת לערוצים/קבוצות.

## הגדרת API שלב אחר שלב

עקבו אחר ההוראות הבאות בקפידה כדי להשיג את פרטי ה-API שלכם:

### 1. בקרו בכלי פיתוח API של My Telegram

פתחו את דפדפן האינטרנט שלכם ונווטו לדף כלי פיתוח ה-API הרשמי של טלגרם: [my.telegram.org](https://my.telegram.org/).

### 2. התחברו לחשבון הטלגרם שלכם

-   הזינו את מספר הטלפון המשויך לחשבון הטלגרם שלכם.
-   לחצו "Next".
-   תקבלו קוד אישור דרך טלגרם. הזינו קוד זה באתר.
-   לחצו "Sign In".

### 3. צרו יישום חדש

לאחר ההתחברות, תראו קטע שכותרתו "API Development Tools".

-   לחצו על "Create new application".
-   מלאו את השדות הנדרשים:
    -   **App title**: הזינו שם תיאורי ליישום שלכם, לדוגמה, `Telegram Downloader App`.
    -   **Short name**: שם קצר וייחודי ליישום שלכם (לדוגמה, `tgdownloader`).
    -   **Platform**: בחרו `Desktop`.
    -   **Description**: (אופציונלי) ספקו תיאור קצר.
-   לחצו "Create Application".

### 4. אחזור פרטי ה-API שלכם

לאחר יצירת היישום, תועברו לדף המציג את פרטי היישום שלכם. כאן תמצאו:

-   **App api_id**: זהו ה-API ID שלכם.
-   **App api_hash**: זהו ה-API Hash שלכם.

**חשוב**: שמרו על פרטים אלו בסודיות. אל תשתפו אותם עם אף אחד ואל תעלו אותם לריפוזיטורים ציבוריים.

### 5. הזינו פרטים ל-Telegram Downloader

-   פתחו את יישום Telegram Downloader.
-   נווטו למסך ההגדרות או ההתקנה הראשונית.
-   הזינו את **API ID**, **API Hash** ומספר ה**טלפון שלכם בטלגרם** לשדות המתאימים.
-   לחצו "שמור" או "התחבר" כדי ליצור את החיבור.

## פתרון בעיות חיבור API

אם אתם נתקלים בבעיות בחיבור ל-API של טלגרם:

-   **בדקו שוב את הפרטים**: ודאו שה-API ID, ה-API Hash ומספר הטלפון שלכם הוזנו נכון.
-   **חיבור לאינטרנט**: ודאו שיש לכם חיבור אינטרנט יציב.
-   **סטטוס חשבון טלגרם**: ודאו שחשבון הטלגרם שלכם פעיל ולא מוגבל.
-   **אימות דו-שלבי (2FA)**: אם הפעלתם 2FA בחשבון הטלגרם שלכם, היישום יבקש מכם את הסיסמה. הזינו אותה כאשר תתבקשו.

אם הבעיות נמשכות, עיינו ב[מדריך פתרון בעיות](TROUBLESHOOTING.md) או דווחו על בעיה ב-GitHub.
