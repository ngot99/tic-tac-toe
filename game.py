from player import Player
from board import Board

class Game:
    def __init__(self):
        self.cont_game = True

        self.players = [Player(), Player()]
        self.current_player = self.players[0]
        self.board = Board()

    def play_game(self):
        self.board.display_board()

        while self.cont_game == True:
            self.board.play_move(self.current_player)
            if self.board.check_winner():
                self.get_Winner()
                self.cont_game = False
            elif self.board.is_full():
                self.cont_game = False
                print("It's a draw")
            else:
                self.switch_player()

            self.board.display_board()
            
    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1] 
        else:
            self.current_player = self.players[0] 

    def get_Winner(self):
        if self.board.win_symbol != '':
            if self.players[0].get_symbol() == self.board.get_win_symbol():
                print(self.players[0].get_name() + " is the winner!")
            else:
                print(self.players[1].get_name() + " is the winner!")
        
    
def main():
    g = Game()
    g.play_game()

    


if __name__ == "__main__":
    main()