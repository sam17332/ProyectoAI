from random import *

class Mat:
    def __init__(self, Mat, dimX, dimY):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY

    def Initiate(self):
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    R.append(randint(1, 9))
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') 
                else:
                    R.append(' ')
            self.Mat.append(R)

    def Get_matrix(self): # Board matrix
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    def Get_currentState(self):
        return Mat(self.Get_matrix(), self.dimX, self.dimY)

    def action(self, i, j):
        Sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        else:
            self.Mat[j][i] = '|'
            if i < self.dimX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]
        return Sum
