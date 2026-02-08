@echo off
title Telegram Downloader v2.1
chcp 65001 >nul
cls
echo.
echo ========================================
echo   Telegram Downloader v2.1
echo   Created by Aviel.AI
echo ========================================
echo.
echo Starting application...
echo.

python telegram_downloader.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo.
    echo Try:
    echo   1. Install dependencies: install.bat
    echo   2. Check Python installation
    echo.
    pause
)
