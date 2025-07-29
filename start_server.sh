#!/bin/bash

# Blackjack Server Startup Script for Raspberry Pi
# This script sets up and runs the blackjack multiplayer game

echo "=== Blackjack Multiplayer Server ==="
echo "Setting up environment..."

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install it first:"
    echo "sudo apt update && sudo apt install python3 python3-pip"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing..."
    sudo apt install python3-pip
fi

# Install required packages
echo "Installing required Python packages..."
pip3 install -r requirements.txt

# Get the local IP address
LOCAL_IP=$(hostname -I | cut -d' ' -f1)

echo ""
echo "=== Setup Complete ==="
echo "Starting Blackjack server..."
echo "Local IP: $LOCAL_IP"
echo "Other devices can connect to: http://$LOCAL_IP:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the application
python3 app.py
