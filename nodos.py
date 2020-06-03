class Thing:
    def __init__(self, currentState):
        self.Current = currentState
        self.CurrentScore = 0
        self.children = {}

    def Make(self, i, j, player): 
        self.children[(i, j)] = Thing(self.Current.Get_currentState())
        mul = 1
        if player:
            mul *= -1
        self.children[(i, j)].CurrentScore = (self.children[(i, j)].Current.action(i, j) * mul) + self.CurrentScore
