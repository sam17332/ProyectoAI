class Convertidor:
        
    def coorTab(x, y):
        tipo = 0
        posi = 0

        #horizontal
        if (x == 1 or x == 3 or x == 5 or x == 7 or x == 9):
            tipo = 0
            if (y == 0):
                if (x == 1):
                    posi = 0
                if (x == 3):
                    posi = 1
                if (x == 5):
                    posi = 2
                if (x == 7):
                    posi = 3
                if (x == 9):
                    posi = 4

            if (y == 2):
                if (x == 1):
                    posi = 5
                if (x == 3):
                    posi = 6
                if (x == 5):
                    posi = 7
                if (x == 7):
                    posi = 8
                if (x == 9):
                    posi = 9

            if (y == 4):
                if (x == 1):
                    posi = 10
                if (x == 3):
                    posi = 11
                if (x == 5):
                    posi = 12
                if (x == 7):
                    posi = 13
                if (x == 9):
                    posi = 14

            if (y == 6):
                if (x == 1):
                    posi = 15
                if (x == 3):
                    posi = 16
                if (x == 5):
                    posi = 17
                if (x == 7):
                    posi = 18
                if (x == 9):
                    posi = 19

            if (y == 8):
                if (x == 1):
                    posi = 20
                if (x == 3):
                    posi = 21
                if (x == 5):
                    posi = 22
                if (x == 7):
                    posi = 23
                if (x == 9):
                    posi = 24

            if (y == 10):
                if (x == 1):
                    posi = 25
                if (x == 3):
                    posi = 26
                if (x == 5):
                    posi = 27
                if (x == 7):
                    posi = 28
                if (x == 9):
                    posi = 29

        #vertical
        if (x == 0 or x == 2 or x == 4 or x == 6 or x == 8 or x == 10):
            tipo = 1
            if (y == 1):
                if (x == 0):
                    posi = 0
                if (x == 2):
                    posi = 1
                if (x == 4):
                    posi = 2
                if (x == 6):
                    posi = 3
                if (x == 8):
                    posi = 4
                if (x == 10):
                    posi = 5

            if (y == 3):
                if (x == 0):
                    posi = 6
                if (x == 2):
                    posi = 7
                if (x == 4):
                    posi = 8
                if (x == 6):
                    posi = 9
                if (x == 8):
                    posi = 10
                if (x == 10):
                    posi = 11

            if (y == 5):
                if (x == 0):
                    posi = 12
                if (x == 2):
                    posi = 13
                if (x == 4):
                    posi = 14
                if (x == 6):
                    posi = 15
                if (x == 8):
                    posi = 16
                if (x == 10):
                    posi = 17

            if (y == 7):
                if (x == 0):
                    posi = 18
                if (x == 2):
                    posi = 19
                if (x == 4):
                    posi = 20
                if (x == 6):
                    posi = 21
                if (x == 8):
                    posi = 22
                if (x == 10):
                    posi = 23

            if (y == 9):
                if (x == 0):
                    posi = 24
                if (x == 2):
                    posi = 25
                if (x == 4):
                    posi = 26
                if (x == 6):
                    posi = 27
                if (x == 8):
                    posi = 28
                if (x == 10):
                    posi = 29
        #print("tipo: " + str(tipo) + " posi: " + str(posi))
        return tipo, posi

    def tabCoor(self, x, y):
        tableroX = 0
        tableroY = 0

        #horizontal
        if (x == 0):
            if (y == 0 or y == 5 or y == 10 or y == 15 or y == 20 or y == 25):
                tableroX = 1
                if (y == 0):
                   tableroY = 0
                elif (y == 5):
                   tableroY = 2 
                elif (y == 10):
                   tableroY = 4 
                elif (y == 15):
                   tableroY = 6 
                elif (y == 20):
                   tableroY = 8
                elif (y == 25):
                   tableroY = 10  

            if (y == 1 or y == 6 or y == 11 or y == 16 or y == 21 or y == 26):
                tableroX = 3
                if (y == 1):
                   tableroY = 0
                elif (y == 6):
                   tableroY = 2 
                elif (y == 11):
                   tableroY = 4 
                elif (y == 16):
                   tableroY = 6 
                elif (y == 21):
                   tableroY = 8
                elif (y == 26):
                   tableroY = 10

            if (y == 2 or y == 7 or y == 12 or y == 17 or y == 22 or y == 27):
                tableroX = 5
                if (y == 2):
                   tableroY = 0
                elif (y == 7):
                   tableroY = 2 
                elif (y == 12):
                   tableroY = 4 
                elif (y == 17):
                   tableroY = 6 
                elif (y == 22):
                   tableroY = 8
                elif (y == 27):
                   tableroY = 10

            if (y == 3 or y == 8 or y == 13 or y == 18 or y == 23 or y == 28):
                tableroX = 7
                if (y == 3):
                   tableroY = 0
                elif (y == 8):
                   tableroY = 2 
                elif (y == 13):
                   tableroY = 4 
                elif (y == 18):
                   tableroY = 6 
                elif (y == 23):
                   tableroY = 8
                elif (y == 28):
                   tableroY = 10

            if (y == 4 or y == 9 or y == 14 or y == 19 or y == 24 or y == 29):
                tableroX = 9
                if (y == 4):
                   tableroY = 0
                elif (y == 9):
                   tableroY = 2 
                elif (y == 14):
                   tableroY = 4 
                elif (y == 19):
                   tableroY = 6 
                elif (y == 24):
                   tableroY = 8
                elif (y == 29):
                   tableroY = 10

        #vertical
        if (x == 1):
            if (y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5):
                tableroY = 1
                if (y == 0):
                    tableroX = 0
                elif (y == 1):
                    tableroX = 2
                elif (y == 2):
                    tableroX = 4
                elif (y == 3):
                    tableroX = 6
                elif (y == 4):
                    tableroX = 8
                elif (y == 5):
                    tableroX = 10

            if (y == 6 or y == 7 or y == 8 or y == 9 or y == 10 or y == 11):
                tableroY = 3
                if (y == 6):
                    tableroX = 0
                elif (y == 7):
                    tableroX = 2
                elif (y == 8):
                    tableroX = 4
                elif (y == 9):
                    tableroX = 6
                elif (y == 10):
                    tableroX = 8
                elif (y == 11):
                    tableroX = 10

            if (y == 12 or y == 13 or y == 14 or y == 15 or y == 16 or y == 17):
                tableroY = 5
                if (y == 12):
                    tableroX = 0
                elif (y == 13):
                    tableroX = 2
                elif (y == 14):
                    tableroX = 4
                elif (y == 15):
                    tableroX = 6
                elif (y == 16):
                    tableroX = 8
                elif (y == 17):
                    tableroX = 10

            if (y == 18 or y == 19 or y == 20 or y == 21 or y == 22 or y == 23):
                tableroY = 7
                if (y == 18):
                    tableroX = 0
                elif (y == 19):
                    tableroX = 2
                elif (y == 20):
                    tableroX = 4
                elif (y == 21):
                    tableroX = 6
                elif (y == 22):
                    tableroX = 8
                elif (y == 23):
                    tableroX = 10

            if (y == 24 or y == 25 or y == 26 or y == 27 or y == 28 or y == 29):
                tableroY = 9
                if (y == 24):
                    tableroX = 0
                elif (y == 25):
                    tableroX = 2
                elif (y == 26):
                    tableroX = 4
                elif (y == 27):
                    tableroX = 6
                elif (y == 28):
                    tableroX = 8
                elif (y == 29):
                    tableroX = 10        
        #print("X: " + str(tableroX) + " Y: " + str(tableroY))
        return tableroX, tableroY
