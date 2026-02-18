@echo off
title Telegram Downloader v2.1.1
chcp 65001 >nul
cls
echo.
echo ========================================
echo   Telegram Downloader v2.1.1
echo   Created by Aviel.AI
echo ========================================
echo.
echo Starting...
echo.

python telegram_downloader.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start
    echo.
    echo Try: install.bat
    echo.
    pause
)
