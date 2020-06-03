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
        return tipo, posi