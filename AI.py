from random import *
import numpy as np
import collections
from minimax import *
from tablero import *
from nodos import *
from convertidor import *

class Tiros:
    def __init__(self):
        currentState = Mat([], 11, 11)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = 2
        self.Score = 0
        self.tabX = 0
        self.tabY = 0
        self.tirosPosiHor = [
            (1, 0),(3,0),(5,0),(7,0),(9,0),(1,2),(3,2),(5,2),(7,2),(9,2),
            (1,4),(3,4),(5,4),(7,4),(9,4),(1,6),(3,6),(5,6),(7,6),(9,6),
            (1,8),(3,8),(5,8),(7,8),(9,8),(1, 10),(3,10),(5,10),(7,10),(9,10)
        ]
        self.tirosPosiVer = [
            (0,1),(0,3),(0,5),(0, 7),(0,9),(2,1),(2,3),(2,5),(2,7),(2,9),
            (4,1),(4,3),(4,5),(4,7),(4,9),(6,1),(6,3),(6,5),(6,7),(6,9),
            (8,1),(8,3),(8,5),(8,7),(8,9),(10, 1),(10,3),(10,5),(10,7),(10,9)
        ]

    def Hum(self):
        horizontal = True
        vertical = True
        tocoHor = False
        tocoVer = False
        HumanX = 0
        HumanY = 0

        if (len(self.tirosPosiHor) == 0):
            horizontal = False

        elif (len(self.tirosPosiVer) == 0):
            vertical = False            


        if (horizontal == True):
            tocoHor = True
            posi = np.random.randint(0,len(self.tirosPosiHor))
            tiro = str(self.tirosPosiHor[posi])
            del self.tirosPosiHor[posi]

        elif (vertical == True):
            tocoVer = True
            posi = np.random.randint(0,len(self.tirosPosiVer))
            tiro = str(self.tirosPosiVer[posi])
            del self.tirosPosiVer[posi]


        if (len(tiro) == 6):
            tiro1 = tiro[1]
            HumanX = int(tiro1)

            tiro2 = tiro[4]
            HumanY = int(tiro2)


        elif (len(tiro) == 7 and tocoHor):
            tiro1 = tiro[1]
            HumanX = int(tiro1)

            tiro2 = tiro[4:6]
            HumanY = int(tiro2)

        elif (len(tiro) == 7 and tocoVer):
            tiro1 = tiro[1:3]
            HumanX = int(tiro1)

            tiro2 = tiro[5]
            HumanY = int(tiro2)

        if (HumanX, HumanY) not in self.State.children:
            self.State.Make(HumanX, HumanY, False)
            self.State = self.State.children[(HumanX, HumanY)]
        else:
            self.State = self.State.children[(HumanX, HumanY)]

        self.Inte()

    def Inte(self):
        move = MiniMax.miniMax(self.State, self.Ply_num)
        self.State = self.State.children[(move[0], move[1])]

        (self.tabX, self.tabY) = Convertidor.coorTab(move[0], move[1])

    def start(self):
        self.Hum()
