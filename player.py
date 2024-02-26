class Player: 
    def __init__(self):
        self.name = str(input("Hello! What is your Name?: "))
        self.valid_symbols = ['X', 'O']
        self.symbol = self.ask_symbol()
        
    def ask_symbol(self):
        while True:
            s =  str(input(self.name + ", would you like to be X or O?: ")).capitalize()
            if s in self.valid_symbols:
                return s
            else:
                print('Invalid symbol, try again!')

    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol