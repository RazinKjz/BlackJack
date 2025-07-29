# Blackjack Server Startup Script for Windows PC (PowerShell)
# This script sets up and runs the blackjack multiplayer game

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "   Blackjack Multiplayer Server" -ForegroundColor Yellow
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Setting up environment..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if pip is available
try {
    $pipVersion = pip --version 2>&1
    Write-Host "Found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "pip is not available. Please reinstall Python with pip included." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Install required packages
Write-Host "`nInstalling required Python packages..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    Write-Host "Packages installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "Failed to install packages. Check your internet connection." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "`n===========================" -ForegroundColor Cyan
Write-Host "      Setup Complete" -ForegroundColor Yellow
Write-Host "===========================" -ForegroundColor Cyan
Write-Host "Starting Blackjack server..." -ForegroundColor Green
Write-Host "`nYour PC is now hosting the game!" -ForegroundColor Yellow
Write-Host "Other devices can connect using the IP addresses shown below." -ForegroundColor White
Write-Host "`nPress Ctrl+C to stop the server" -ForegroundColor Magenta
Write-Host ""

# Run the application
try {
    python app.py
} catch {
    Write-Host "`nServer stopped or encountered an error." -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
