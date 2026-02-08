@echo off
echo Building Telegram Downloader EXE...
pip install pyinstaller
pyinstaller --onefile --windowed --name "TelegramDownloader" telegram_downloader.py
echo Done! Check the dist folder.
pause
