import socket
import threading
import random

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5555

players = {}
lock = threading.Lock()
dealer_hand = []

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    while 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def handle_client(conn, addr, player_name):
    print(f"[NEW CONNECTION] {player_name} connected from {addr}")
    conn.sendall(f"Welcome, {player_name}! Waiting for the game to start...\n".encode())

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if data:
                with lock:
                    players[player_name]['action'] = data
        except:
            print(f"[DISCONNECTED] {player_name}")
            break

def broadcast(msg):
    for p in players.values():
        p['conn'].sendall(msg.encode())

def start_game():
    global dealer_hand
    dealer_hand = [deal_card(), deal_card()]
    broadcast(f"\nGame starting! Dealer's visible card: {dealer_hand[0]}")

    # Deal cards to each player
    for name, p in players.items():
        p['hand'] = [deal_card(), deal_card()]
        p['action'] = ''
        hand_str = f"Your hand: {p['hand']} (score: {calculate_score(p['hand'])})"
        p['conn'].sendall(hand_str.encode())

    # Players take turns
    for name, p in players.items():
        while True:
            p['conn'].sendall("\nYour turn! Type 'hit' or 'stand': ".encode())
            while p['action'] == '':
                pass  # wait for input
            action = p['action']
            p['action'] = ''
            if action == 'hit':
                card = deal_card()
                p['hand'].append(card)
                score = calculate_score(p['hand'])
                p['conn'].sendall(f"You drew {card}. Your hand: {p['hand']} (score: {score})".encode())
                if score >= 21:
                    break
            elif action == 'stand':
                break

    # Dealer's turn
    dealer_score = calculate_score(dealer_hand)
    broadcast(f"\nDealer's hand: {dealer_hand} (score: {dealer_score})")
    while dealer_score < 17:
        card = deal_card()
        dealer_hand.append(card)
        dealer_score = calculate_score(dealer_hand)
        broadcast(f"Dealer draws {card}. Dealer's hand: {dealer_hand} (score: {dealer_score})")

    # Results
    broadcast("\n=== Results ===")
    for name, p in players.items():
        player_score = calculate_score(p['hand'])
        msg = f"{name}'s hand: {p['hand']} (score: {player_score})\n"
        if player_score > 21:
            msg += f"{name} busted! You lose."
        elif dealer_score > 21:
            msg += f"Dealer busted! {name} wins!"
        elif player_score == dealer_score:
            msg += f"{name} draws with dealer."
        elif player_score > dealer_score:
            msg += f"{name} wins!"
        else:
            msg += f"{name} loses."
        p['conn'].sendall(msg.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        conn.sendall("Enter your name: ".encode())
        name = conn.recv(1024).decode().strip()
        with lock:
            players[name] = {'conn': conn, 'hand': [], 'action': ''}
        thread = threading.Thread(target=handle_client, args=(conn, addr, name))
        thread.start()

        if len(players) >= 2:  # Start game when at least 2 players join
            start_game()

if __name__ == "__main__":
    main()
