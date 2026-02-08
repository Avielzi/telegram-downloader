@echo off
title Repair Installation
color 0E
echo.
echo ========================================
echo   Repair Installation
echo   Created by Aviel.AI
echo ========================================
echo.
echo This will reinstall all packages.
echo.
pause

echo.
echo [1/2] Uninstalling old packages...
pip uninstall PyQt6 telethon cryptg -y

echo.
echo [2/2] Installing fresh packages...
pip install PyQt6 telethon cryptg --upgrade --force-reinstall

if errorlevel 1 (
    echo.
    echo ERROR: Repair failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Repair complete!
echo ========================================
echo.
echo All packages reinstalled.
echo You can now run the application.
echo.
pause
