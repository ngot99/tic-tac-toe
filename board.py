from player import Player
#from game.py import Game

class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.win_symbol = ''

    def display_board(self):
        #print("_________________")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print("| " + self.board[i][j] , end=" | ")
            print()

    def play_move(self, player):
        turn = True
        while turn == True:
            row, col = (input(player.get_name() + ", make a move. What location? (row,col): ")).split(",")
            row, col = int(row), int(col)
            if self.is_valid(row,col):
                self.board[row][col] = player.get_symbol()
                turn = False
            else:
                print("Invalid Move! Try again")
    
    def is_valid(self,row,col):
        return self.board[row][col] == ' '

    def get_win_symbol(self):
        return self.win_symbol

    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ' ':
                    return False
        else:
            return True

    def check_winner(self):
        ''' 
        8 ways to win
        there must be an optimal way to check if there is a winner, figure during optimization
        check each win condition
        '''

        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            self.win_symbol = self.board[0][0]
            return True
            
        elif self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]and self.board[1][0] != ' ':
            self.win_symbol = self.board[1][0]
            return True
            
        elif self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            self.win_symbol = self.board[2][0]
            return True

        # Check vertical
        elif self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]and self.board[0][0] != ' ':
            self.win_symbol = self.board[0][0]
            return True
            
        elif self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]and self.board[0][1] != ' ':
            self.win_symbol = self.board[0][1]
            return True
            
        elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]and self.board[0][2] != ' ':
            self.win_symbol = self.board[0][2]
            return True

        # Check diagonal
        elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]and self.board[0][0] != ' ':
            self.win_symbol = self.board[0][0]
            return True
            
        elif self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]and self.board[2][0] != ' ':
            self.win_symbol = self.board[2][0]
            return True
        
        return False   