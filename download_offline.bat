@echo off
title Offline Package Downloader
echo.
echo ========================================
echo   Offline Package Downloader
echo   Created by Aviel.AI
echo ========================================
echo.
echo This will download all packages
echo for offline installation.
echo.
pause

REM Create directory
if not exist "offline_packages" mkdir offline_packages

echo.
echo Downloading packages...
echo.

REM Download
pip download -r requirements.txt -d offline_packages

if errorlevel 1 (
    echo.
    echo ERROR: Download failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Download complete!
echo ========================================
echo.
echo Packages saved to: offline_packages\
echo.
echo To install offline:
echo   pip install --no-index --find-links=offline_packages -r requirements.txt
echo.
pause
