import socketio
import numpy as np
import random
from AI import *
from board import *


sio = socketio.Client()

class infoGame:
    def __init__(self):
        self.Match = Tiros()
        self.username = ""
        self.tournament_id = ""
        self.game_id = ""
        self.board = []
        self.ready = False
        self.game_finished = False
        self.player_turn_id = 0

@sio.on('connect')
def onConnect():
    print('Connected user: '+infoGame.username)
    sio.emit('signin',{
        'user_name': infoGame.username,
        'tournament_id': infoGame.tournament_id,
        'user_role': 'player'
    })

@sio.event
def conn_error():
    print("Connection failed")

@sio.event
def disconnect():
    print("Disconnected")

@sio.on('ready')
def ready(server):
    movement = []
    infoGame.game_id = server['game_id']
    infoGame.player_turn_id = server['player_turn_id']
    infoGame.board = server['board']
    infoGame.game_finished = False
    infoGame.ready = True
    cont = 0

    for i in range(len(infoGame.board)):
        for j in range(len(infoGame.board[i])):
            if(infoGame.board[i][j] == 99):
                cont += 1
                tiro1 = i
                tiro2 = j
    if cont <= 20:
        typeLine = tiro1
        position = tiro2
        movement = [typeLine,position]
    else:
        infoGame.Match.start()
        typeLine = infoGame.Match.tabX
        position = infoGame.Match.tabY
        movement = [typeLine,position]


    print("Movement: " + str(movement[0]) + ", " + str(movement[1]))

    sio.emit('play',{
        'player_turn_id':infoGame.player_turn_id,
        'tournament_id': infoGame.tournament_id,
        'game_id': infoGame.game_id,
        'movement': movement
    })

def reset():
    row = np.ones(30) * 99
    infoGame.board = [np.ndarray.tolist(row), np.ndarray.tolist(row)]
    infoGame.Match = Tiros()

@sio.on('finish')
def finish(server):
    reset()
    
    if server['player_turn_id'] == server['winner_turn_id']:
        print("Eres el ganador")
    else:
        print("Perdiste")
    print('Juego termiando!')
    infoGame.gameFinished = True
    sio.emit('player_ready',{
        'tournament_id': infoGame.tournament_id,
        'game_id': infoGame.game_id,
        'player_turn_id': server['player_turn_id']
    })


infoGame = infoGame()
infoGame.username = input("Ingrese usuario: \n")
infoGame.tournament_id = input("Ingrese el tournament ID: \n")
host = input("Ingrese el host: \n")
sio.connect(host)