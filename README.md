# Blackjack Multiplayer Game for Raspberry Pi & PC

A Flask-SocketIO based multiplayer blackjack game designed to run on both Raspberry Pi and PC, allowing other devices to connect and play over the local network.

## Features

- Multiplayer blackjack game (2 players)
- Real-time game updates using WebSockets
- Mobile-friendly web interface
- Cross-platform: Works on Raspberry Pi, Windows PC, Mac, and Linux
- Automatic platform detection and configuration
- Other devices can connect over WiFi/LAN

## Requirements

- **Raspberry Pi:** Any model with network connectivity
- **PC:** Windows 10/11, macOS, or Linux
- Python 3.7 or higher
- Active internet connection for initial setup
- All devices must be on the same network

## Installation & Setup

### On Raspberry Pi:

1. **Update your Raspberry Pi:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and pip (if not already installed):**
   ```bash
   sudo apt install python3 python3-pip -y
   ```

3. **Navigate to the project directory:**
   ```bash
   cd BlackJack
   ```

4. **Install required packages:**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Make the startup script executable:**
   ```bash
   chmod +x start_server.sh
   ```

### On Windows PC:

1. **Install Python:**
   - Download from [python.org](https://python.org)
   - ⚠️ **Important:** Check "Add Python to PATH" during installation

2. **Open Command Prompt or PowerShell in the project folder**

3. **Install required packages:**
   ```cmd
   pip install -r requirements.txt
   ```

### On Mac/Linux PC:

1. **Ensure Python 3 is installed:**
   ```bash
   python3 --version
   ```

2. **Install required packages:**
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Game

### Raspberry Pi:
```bash
./start_server.sh
```

### Windows PC:
**Option 1 - Batch file (double-click):**
```cmd
start_server.bat
```

**Option 2 - PowerShell (recommended):**
```powershell
.\start_server.ps1
```

**Option 3 - Command line:**
```cmd
python app.py
```

### Mac/Linux PC:
```bash
python3 app.py
```

## Connecting Other Devices

1. **Start the server** on your host device (Raspberry Pi or PC)

2. **Note the IP address displayed** when the server starts
   - The application automatically detects and shows available network connections
   - Example output: `Main IP: http://192.168.1.100:5000`

3. **On other devices (phones, tablets, computers):**
   - Connect to the same WiFi network as the host
   - Open a web browser
   - Navigate to the displayed IP address
   - Example: `http://192.168.1.100:5000`

4. **Join the game:**
   - Enter your name
   - Click "Join Game"
   - Wait for another player to join
   - Game starts automatically when 2 players are connected

## Game Rules

- Standard Blackjack rules
- Goal: Get as close to 21 as possible without going over
- Face cards (J, Q, K) = 10 points
- Aces = 11 points (automatically converts to 1 if needed)
- Players take turns to Hit (draw card) or Stand (keep current hand)
- Winner has the highest score ≤ 21

## Troubleshooting

### Can't connect from other devices:
- Ensure all devices are on the same WiFi network
- Check Raspberry Pi firewall settings: `sudo ufw status`
- If firewall is active, allow port 5000: `sudo ufw allow 5000`

### Game doesn't start:
- Refresh the browser page
- Check the Raspberry Pi terminal for error messages
- Ensure both players have different names

### Python package errors:
- Update pip: `pip3 install --upgrade pip`
- Reinstall requirements: `pip3 install -r requirements.txt --force-reinstall`

## Network Security

This application is designed for local network use only. For security:
- Only run on trusted local networks
- Do not expose to the internet without proper security measures
- Consider changing the SECRET_KEY in app.py for production use

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## File Structure

```
BlackJack/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── start_server.sh     # Startup script
├── README.md          # This file
└── templates/
    └── index.html     # Web interface
```

## Technical Details

- **Framework:** Flask with SocketIO for real-time communication
- **Port:** 5000 (configurable in app.py)
- **Host:** 0.0.0.0 (listens on all network interfaces)
- **CORS:** Enabled for cross-origin requests

Enjoy your Raspberry Pi blackjack game!
