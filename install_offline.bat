@echo off
title Offline Installation
echo.
echo ========================================
echo   Offline Installation
echo   Created by Aviel.AI
echo ========================================
echo.

REM Check if offline packages exist
if not exist "offline_packages" (
    echo ERROR: offline_packages folder not found!
    echo.
    echo Please run download_offline.bat first
    echo or copy the offline_packages folder here.
    echo.
    pause
    exit /b 1
)

echo Installing from offline packages...
echo.

pip install --no-index --find-links=offline_packages -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Installation complete!
echo ========================================
echo.
pause
