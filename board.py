from player import Player
#from game.py import Game

class Board:
    def __init__(self):
        self.board = [['0'] *3 ] * 3
        self.winner = False
  

    def displayBoard(self):
        #print("_________________")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print("| " + self.board[i][j] , end=" | ")
            #print()
            #print("_________________")

    def isValid(self,row,col):
        return self.board[row][col] == '0'

    def playMove(self, player):
        turn = True
        row,col = player.makeMove()
        print(row,col)
        if self.isValid(row,col):
            print(self.board[row][col])
            self.board[row][col] = player.getSymbol()
            print(self.board[1][col])
            turn = False
        else:
            print("Invalid Move! Try again")

    def checkWinner(self):
        # 8 ways to win
        # there must be an optimal way to check if there is a winner, figure that out later
        # check each win condition
        # Check horizontal
        if self.board[0] == self.board[1] and self.board[0] == self.board[2]:
            self.winner = True
            
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            self.winner = True
            
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            self.winner = True
            

        # Check vertical
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            self.winner = True
            
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            self.winner = True
            
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            self.winner = True
            

        # Check diagonal
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            self.winner = True
            
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            self.winner = True
            
        return self.winner

def main():
    b = Board()
    p1 = Player()
    b.displayBoard()
    b.playMove(p1)
    b.displayBoard()



if __name__ == "__main__":
    main()
