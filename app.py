from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

players = []
hands = {}
current_player_index = 0
deck = []
game_started = False

def create_deck():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(cards)
    return cards

def deal_card():
    return deck.pop()

def calculate_score(hand):
    score = sum(hand)
    aces = hand.count(11)
    while score > 21 and aces:
        score -= 10
        aces -=1
    return score

def next_player():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)

def broadcast_game_state():
    state = []
    for p in players:
        state.append({
            'sid': p['sid'],
            'name': p['name'],
            'hand': hands[p['sid']],
            'score': calculate_score(hands[p['sid']]),
            'is_current': players[current_player_index]['sid'] == p['sid']
        })
    socketio.emit('game_state', state)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    global game_started
    sid = request.sid  # Correct way to get the session id
    name = data['name']

    if game_started:
        emit('message', 'Game already started, please wait for next round.')
        return

    if len(players) >= 2:
        emit('message', 'Game full! Try again later.')
        return

    players.append({'sid': sid, 'name': name})
    hands[sid] = []

    print(f'{name} joined the game.')

    if len(players) == 2:
        game_started = True
        global deck
        deck = create_deck()
        for p in players:
            hands[p['sid']] = [deal_card(), deal_card()]
        current_player_index = 0
        broadcast_game_state()
        socketio.emit('message', 'Game started!')
        socketio.emit('your_turn', players[current_player_index]['sid'])
    else:
        emit('message', 'Waiting for another player...')

@socketio.on('hit')
def on_hit():
    global game_started
    sid = str(socketio.sid)
    if not game_started or players[current_player_index]['sid'] != sid:
        return

    hands[sid].append(deal_card())
    score = calculate_score(hands[sid])
    broadcast_game_state()

    if score > 21:
        socketio.emit('message', f'{players[current_player_index]["name"]} busted!')
        next_player()
        socketio.emit('your_turn', players[current_player_index]['sid'])
    elif score == 21:
        socketio.emit('message', f'{players[current_player_index]["name"]} hit 21!')
        next_player()
        socketio.emit('your_turn', players[current_player_index]['sid'])

@socketio.on('stand')
def on_stand():
    global game_started
    sid = str(socketio.sid)
    if not game_started or players[current_player_index]['sid'] != sid:
        return

    socketio.emit('message', f'{players[current_player_index]["name"]} stands.')
    next_player()

    if current_player_index == 0:
        # Game over
        results = []
        for p in players:
            score = calculate_score(hands[p['sid']])
            results.append({'name': p['name'], 'score': score})
        winner = None
        high_score = 0
        for r in results:
            if r['score'] <= 21 and r['score'] > high_score:
                high_score = r['score']
                winner = r['name']
        if winner:
            socketio.emit('message', f'Game over! Winner is {winner} with {high_score} points.')
        else:
            socketio.emit('message', 'Game over! No winners, everyone busted.')

        # Reset game
        reset_game()
    else:
        socketio.emit('your_turn', players[current_player_index]['sid'])
    broadcast_game_state()

@socketio.on('disconnect')
def on_disconnect():
    global game_started
    sid = str(socketio.sid)
    leaving_player = next((p for p in players if p['sid'] == sid), None)
    if leaving_player:
        print(f'{leaving_player["name"]} disconnected.')
        players.remove(leaving_player)
        hands.pop(sid, None)
        game_started = False
        socketio.emit('message', 'Game ended because a player left.')
        broadcast_game_state()

def reset_game():
    global players, hands, deck, current_player_index, game_started
    players = []
    hands = {}
    deck = []
    current_player_index = 0
    game_started = False

if __name__ == '__main__':
    socketio.run(app, debug=True)
