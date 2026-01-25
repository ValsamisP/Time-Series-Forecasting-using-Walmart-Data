@echo off
REM Setup script for Windows
REM Usage: setup.bat

echo ==================================================
echo  Walmart Forecasting Project Setup
echo  Platform: Windows
echo ==================================================

REM Check if Python is installed
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

python --version
echo [OK] Python found

REM Remove old virtual environment if exists
if exist venv (
    echo.
    echo Found existing virtual environment
    set /p REMOVE="Do you want to remove it and create a fresh one? (y/n): "
    if /i "%REMOVE%"=="y" (
        echo Removing old virtual environment...
        rmdir /s /q venv
    ) else (
        echo Keeping existing virtual environment
    )
)

REM Create virtual environment
if not exist venv (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [OK] Pip upgraded

REM Install dependencies
echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [WARNING] Some packages failed to install
    echo Trying with --prefer-binary flag...
    pip install --prefer-binary -r requirements.txt
)

echo.
echo [OK] Dependencies installed

REM Run environment check
echo.
echo Running environment check...
python check_environment.py

echo.
echo ==================================================
echo  Setup Complete!
echo ==================================================
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate
echo.
echo To run Jupyter notebooks:
echo   jupyter notebook
echo.
echo To run Quarto documents:
echo   cd myquarto
echo   quarto preview Part1.qmd
echo.
echo ==================================================
pause