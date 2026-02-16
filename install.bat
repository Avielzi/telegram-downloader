@echo off
title Telegram Downloader - Installation
chcp 65001 >nul
color 0A
cls

echo.
echo ========================================
echo   Telegram Downloader v3.5
echo   Installation
echo   Created by Aviel.AI
echo ========================================
echo.

REM Check Python
echo [1/5] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python NOT found!
    echo.
    echo Please install Python 3.8+ from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check the box during install:
    echo [X] Add Python to PATH
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo    OK - Python %PYTHON_VERSION% found
echo.

REM Check pip
echo [2/5] Checking pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo    ERROR - pip not found!
    echo    Attempting to install pip...
    python -m ensurepip --default-pip
    if errorlevel 1 (
        echo    FAILED - Could not install pip
        echo    Please reinstall Python with pip enabled
        pause
        exit /b 1
    )
)
echo    OK - pip is available
echo.

REM Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo    WARNING - Could not upgrade pip
) else (
    echo    OK - pip upgraded
)
echo.

REM Install packages
echo [4/5] Installing packages...
echo    This may take a few minutes...
echo.

echo    Installing PyQt6...
python -m pip install PyQt6 --quiet
if errorlevel 1 (
    echo    ERROR - PyQt6 installation failed!
    goto :install_error
) else (
    echo    OK - PyQt6 installed
)

echo    Installing Telethon...
python -m pip install telethon --quiet
if errorlevel 1 (
    echo    ERROR - Telethon installation failed!
    goto :install_error
) else (
    echo    OK - Telethon installed
)

echo    Installing cryptg...
python -m pip install cryptg --quiet
if errorlevel 1 (
    echo    WARNING - cryptg failed (optional)
) else (
    echo    OK - cryptg installed
)

echo.
echo    All packages installed!
echo.

REM Verify
echo [5/5] Verifying...
python -c "import PyQt6.QtWidgets; import telethon" 2>nul
if errorlevel 1 (
    echo    ERROR - Verification failed!
    pause
    exit /b 1
)
echo    OK - Verification complete
echo.
echo.

echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo You can now run:
echo   - Double-click: run.bat
echo   - Or: python telegram_downloader.py
echo.
echo Next steps:
echo   1. Run the application
echo   2. Get API from my.telegram.org
echo   3. Start downloading!
echo.
echo ----------------------------------------
echo Created by Aviel.AI
echo ----------------------------------------
echo.
pause
exit /b 0

:install_error
echo.
echo ========================================
echo   Installation Failed!
echo ========================================
echo.
echo Try these solutions:
echo   1. Check internet connection
echo   2. Run as Administrator
echo   3. Manual install: pip install -r requirements.txt
echo   4. Update Python to latest version
echo.
echo If problems persist:
echo   - Check README.md
echo   - Open GitHub issue
echo.
pause
exit /b 1
