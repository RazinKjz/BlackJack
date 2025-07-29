@echo off
REM Blackjack Server Startup Script for Windows PC
REM This script sets up and runs the blackjack multiplayer game

echo ====================================
echo   Blackjack Multiplayer Server
echo ====================================
echo Setting up environment...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not available. Please reinstall Python with pip included.
    pause
    exit /b 1
)

REM Install required packages
echo Installing required Python packages...
pip install -r requirements.txt

echo.
echo ===========================
echo      Setup Complete
echo ===========================
echo Starting Blackjack server...
echo.
echo Your PC is now hosting the game!
echo Other devices can connect using the IP addresses shown below.
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the application
python app.py

pause
