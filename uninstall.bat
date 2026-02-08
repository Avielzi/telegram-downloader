@echo off
title הסרת Telegram Downloader
chcp 65001 >nul
echo.
echo ========================================
echo   הסרת Telegram Downloader
echo ========================================
echo.
echo נוצר על ידי Aviel.AI
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python לא מותקן!
    pause
    exit /b 1
)

python uninstall.py

pause
