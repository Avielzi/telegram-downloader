@echo off
title Check Dependencies
echo.
echo ========================================
echo   Dependency Check
echo   Created by Aviel.AI
echo ========================================
echo.

REM Check Python
echo Checking Python...
python --version 2>nul
if errorlevel 1 (
    echo    [X] Python NOT found
    set PYTHON_OK=0
) else (
    echo    [OK] Python installed
    set PYTHON_OK=1
)
echo.

REM Check pip
echo Checking pip...
pip --version 2>nul
if errorlevel 1 (
    echo    [X] pip NOT found
    set PIP_OK=0
) else (
    echo    [OK] pip available
    set PIP_OK=1
)
echo.

REM Check PyQt6
echo Checking PyQt6...
python -c "import PyQt6.QtWidgets" 2>nul
if errorlevel 1 (
    echo    [X] PyQt6 NOT installed
    set PYQT6_OK=0
) else (
    python -c "import PyQt6; print('    [OK] PyQt6 version:', PyQt6.QtCore.PYQT_VERSION_STR)"
    set PYQT6_OK=1
)
echo.

REM Check Telethon
echo Checking Telethon...
python -c "import telethon" 2>nul
if errorlevel 1 (
    echo    [X] Telethon NOT installed
    set TELETHON_OK=0
) else (
    python -c "import telethon; print('    [OK] Telethon version:', telethon.__version__)"
    set TELETHON_OK=1
)
echo.

REM Check cryptg
echo Checking cryptg (optional)...
python -c "import cryptg" 2>nul
if errorlevel 1 (
    echo    [!] cryptg not installed (optional)
    set CRYPTG_OK=0
) else (
    echo    [OK] cryptg installed
    set CRYPTG_OK=1
)
echo.

REM Summary
echo ========================================
echo   Summary:
echo ========================================

if %PYTHON_OK%==1 (
    echo  [OK] Python
) else (
    echo  [X] Python
)

if %PIP_OK%==1 (
    echo  [OK] pip
) else (
    echo  [X] pip
)

if %PYQT6_OK%==1 (
    echo  [OK] PyQt6
) else (
    echo  [X] PyQt6
)

if %TELETHON_OK%==1 (
    echo  [OK] Telethon
) else (
    echo  [X] Telethon
)

if %CRYPTG_OK%==1 (
    echo  [OK] cryptg
) else (
    echo  [!] cryptg (optional)
)

echo.

REM Final check
if %PYTHON_OK%==1 if %PIP_OK%==1 if %PYQT6_OK%==1 if %TELETHON_OK%==1 (
    echo ========================================
    echo   All dependencies installed!
    echo ========================================
    echo.
    echo Ready to run Telegram Downloader
    echo.
) else (
    echo ========================================
    echo   Missing dependencies!
    echo ========================================
    echo.
    echo Please run: install.bat
    echo.
)

pause
