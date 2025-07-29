# Blackjack Multiplayer Game for Raspberry Pi

A Flask-SocketIO based multiplayer blackjack game designed to run on a Raspberry Pi, allowing other devices to connect and play over the local network.

## Features

- Multiplayer blackjack game (2 players)
- Real-time game updates using WebSockets
- Mobile-friendly web interface
- Runs on Raspberry Pi
- Other devices can connect over WiFi/LAN

## Requirements

- Raspberry Pi (any model with network connectivity)
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

3. **Clone or copy the project files to your Raspberry Pi**

4. **Navigate to the project directory:**
   ```bash
   cd BlackJack
   ```

5. **Install required packages:**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Make the startup script executable:**
   ```bash
   chmod +x start_server.sh
   ```

## Running the Game

### Option 1: Using the startup script (Recommended)
```bash
./start_server.sh
```

### Option 2: Direct Python execution
```bash
python3 app.py
```

## Connecting Other Devices

1. **Start the server on your Raspberry Pi** (see above)

2. **Find your Raspberry Pi's IP address:**
   - The startup script will display it
   - Or run: `hostname -I | cut -d' ' -f1`
   - Example: `192.168.1.100`

3. **On other devices (phones, tablets, computers):**
   - Open a web browser
   - Navigate to: `http://[PI_IP_ADDRESS]:5000`
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
