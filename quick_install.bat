@echo off
title Quick Install
echo.
echo ========================================
echo   Quick Install
echo   Created by Aviel.AI
echo ========================================
echo.
echo Installing packages...
echo.

pip install PyQt6 telethon cryptg --upgrade

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    echo Try: install.bat for detailed install
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Installation complete!
echo ========================================
echo.
pause
