class Player: 
    def __init__(self):
        self.name = str(input("Hello! What is your Name?: "))
        self.symbol = str(input(self.name + ", would you like to be X or O?: "))        

    def getName(self):
        return self.name
    
    def getSymbol(self):
        return self.symbol
    
    def makeMove(self):
        row = int(input("What row 0-2?: "))
        col = int(input("what col 0-2?: "))
        return row,col
