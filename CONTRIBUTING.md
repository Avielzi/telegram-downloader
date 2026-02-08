# 🤝 Contributing to Telegram Downloader

We welcome contributions from everyone! By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🐛 How to Report Bugs

If you find a bug, please open an issue on our [GitHub Issues page](https://github.com/Avielzi/telegram-downloader/issues) and use the `bug_report.md` template. Before opening a new issue, please check if a similar issue already exists.

When reporting a bug, please include:
- A clear and concise description of the bug.
- Steps to reproduce the behavior.
- Expected behavior.
- Actual behavior.
- Screenshots or GIFs if applicable.
- Your operating system and Python version.

## ✨ How to Suggest Features

We love new ideas! If you have a feature request, please open an issue on our [GitHub Issues page](https://github.com/Avielzi/telegram-downloader/issues) and use the `feature_request.md` template.

When suggesting a feature, please include:
- A clear and concise description of the proposed feature.
- Why this feature would be useful.
- Any alternative solutions you've considered.

## 💻 Code Style Guidelines

To maintain code readability and consistency, please follow these guidelines:
-   **Python**: Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
-   **Formatting**: Use `black` for automatic code formatting.
-   **Linting**: Use `flake8` to check for style guide violations.

## 🌿 Git Workflow

We use a standard Git workflow:

1.  **Fork** the repository.
2.  **Clone** your forked repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/telegram-downloader.git
    cd telegram-downloader
    ```
3.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/your-bug-fix-name
    ```
4.  **Make your changes** and commit them with clear, concise messages (see [Commit Messages](#commit-messages)).
5.  **Push your branch** to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```
6.  **Open a Pull Request (PR)** to the `main` branch of the original repository. Provide a clear description of your changes.

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. Examples:

-   `feat(ui): add dark mode support`
-   `fix(download): resolve async event loop error`
-   `docs(readme): update installation guide`
-   `refactor(scan): improve media detection`
-   `test(integration): add download tests`
-   `chore(deps): update dependencies`

## 🛠️ Building from Source

To build the application from source, you'll need Python 3.8+ and the development dependencies. First, install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

Then, you can run the application directly:

```bash
python telegram_downloader.py
```

## 🧪 Running Tests

To run the tests, navigate to the project root and execute:

```bash
pytest tests/
```

## 🌐 Translation Guidelines

If you wish to contribute translations or improve existing ones, please refer to `i18n.py` and submit your changes via a Pull Request. New languages are always welcome!

---

## 🇮🇱 תרומה לפרויקט Telegram Downloader

אנו מברכים על תרומות מכולם! על ידי השתתפות בפרויקט זה, אתם מסכימים לציית ל[קוד ההתנהגות](CODE_OF_CONDUCT.md) שלנו.

## 🐛 איך לדווח על באגים

אם מצאתם באג, אנא פתחו גיליון (issue) בדף [GitHub Issues](https://github.com/Avielzi/telegram-downloader/issues) שלנו והשתמשו בתבנית `bug_report.md`. לפני פתיחת גיליון חדש, אנא בדקו אם גיליון דומה כבר קיים.

בעת דיווח על באג, אנא כללו:
- תיאור ברור ותמציתי של הבאג.
- שלבים לשחזור ההתנהגות.
- התנהגות צפויה.
- התנהגות בפועל.
- צילומי מסך או קובצי GIF אם רלוונטי.
- מערכת ההפעלה וגרסת הפייתון שלכם.

## ✨ איך להציע תכונות

אנחנו אוהבים רעיונות חדשים! אם יש לכם בקשה לתכונה, אנא פתחו גיליון בדף [GitHub Issues](https://github.com/Avielzi/telegram-downloader/issues) שלנו והשתמשו בתבנית `feature_request.md`.

בעת הצעת תכונה, אנא כללו:
- תיאור ברור ותמציתי של התכונה המוצעת.
- מדוע תכונה זו תהיה שימושית.
- כל פתרונות חלופיים ששקלתם.

## 💻 הנחיות סגנון קוד

כדי לשמור על קריאות ועקביות הקוד, אנא עקבו אחר ההנחיות הבאות:
-   **פייתון**: הקפידו על [PEP 8](https://www.python.org/dev/peps/pep-0008/) עבור קוד פייתון.
-   **עיצוב**: השתמשו ב-`black` לעיצוב קוד אוטומטי.
-   **בדיקת סגנון**: השתמשו ב-`flake8` לבדיקת הפרות של מדריך הסגנון.

## 🌿 תהליך עבודה עם Git

אנו משתמשים בתהליך עבודה סטנדרטי עם Git:

1.  **בצעו Fork** לריפוזיטורי.
2.  **שכפלו** את הריפוזיטורי המפורק שלכם:
    ```bash
    git clone https://github.com/YOUR_USERNAME/telegram-downloader.git
    cd telegram-downloader
    ```
3.  **צרו ענף חדש** עבור התכונה או תיקון הבאג שלכם:
    ```bash
    git checkout -b feature/your-feature-name
    # או
    git checkout -b bugfix/your-bug-fix-name
    ```
4.  **בצעו את השינויים שלכם** ובצעו להם Commit עם הודעות ברורות ותמציתיות (ראו [הודעות Commit](#הודעות-commit)).
5.  **דחפו את הענף שלכם** לריפוזיטורי המפורק שלכם:
    ```bash
    git push origin feature/your-feature-name
    ```
6.  **פתחו בקשת משיכה (PR)** לענף ה-`main` של הריפוזיטורי המקורי. ספקו תיאור ברור של השינויים שלכם.

### הודעות Commit

אנו עוקבים אחר מפרט [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). דוגמאות:

-   `feat(ui): add dark mode support`
-   `fix(download): resolve async event loop error`
-   `docs(readme): update installation guide`
-   `refactor(scan): improve media detection`
-   `test(integration): add download tests`
-   `chore(deps): update dependencies`

## 🛠️ בנייה מקוד מקור

כדי לבנות את היישום מקוד מקור, תצטרכו Python 3.8+ ותלויות הפיתוח. ראשית, התקינו את תלויות הפיתוח:

```bash
pip install -r requirements-dev.txt
```

לאחר מכן, תוכלו להפעיל את היישום ישירות:

```bash
python telegram_downloader.py
```

## 🧪 הרצת בדיקות

כדי להריץ את הבדיקות, נווטו לשורש הפרויקט והריצו:

```bash
pytest tests/
```

## 🌐 הנחיות תרגום

אם ברצונכם לתרום תרגומים או לשפר תרגומים קיימים, אנא עיינו בקובץ `i18n.py` ושלחו את השינויים שלכם באמצעות בקשת משיכה.
