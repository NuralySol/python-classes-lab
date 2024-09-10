# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It’s player X’s turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.

# Creating a tic-tac-toe game in python
# Need to define a Board class and set the rules of the game

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range (3)] for _ in range (3)]
        
    def print_board(self):
        print(" A B C ")
        for i, row in enumerate(self.board):
            print(f"{i+1}{row[0]} | {row[1]} | {row [2]}")
            if i < 2:
                print (" ---+---+---")
    
    def make_move(self, row, col, player_symbol):
        if self.board [row][col] == ' ':
            self.board [row][col] = player_symbol
            return True
        else:
            print("Cell is already occupied, choose another move.")
            return False
    
    def is_winner(self, player_symbol):
        for row in self.board:
            if all([cell == player_symbol for cell in row]):
                return True
            
        for col in range(3):
            if all ([self.board[row][col] == player_symbol for row in range(3)]):
                return True
            
        if self.board[0][0] == player_symbol and self.board[1][1] == player_symbol and self.board [2][2] == player_symbol:
            return True
        if self.board[0][2] == player_symbol and self.board[1][1] == player_symbol and self.board [2][0] == player_symbol:
            return True
            
        return False
        
    def is_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)
            
# Need to set up a player to play the game to init with a name and a symbol X or O

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

# Need to set a Game class for the game itself

class Game:
    def __init__(self):
        self.board = Board()
        self.player_x = Player("Player X", 'X')
        self.player_o = Player("Player O", 'O')
        self.current_player = self.player_x # Player x starts the game first 
        
    def switch_player(self):
        self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
        

    def get_move(self):
        while True:
            move = input(f"f{self.current_player.name}, enter your move e.g A1 or B2 please refert to the output: ").upper()
            
            if len(move) != 2 or move[0] not in 'ABC' or move[1] not in '123':
                print('invalid input. Please enter in the format A1, B2, etc.')
                continue
            
            col = ord(move[0]) - ord('A')
            row = int(move[1]) - 1
            
            if self.board.make_move(row, col, self.current_player.symbol):
                break
    
    def check_winner_or_tie(self):
        if self.board.is_winner(self.current_player.symbol):
            self.board.print_board()
            print(f"Congratulations {self.current_player.name}, you won!")
            return True
        
        if self.board.is_full():
            self.board.print_board()
            print("It's a Tie!")
            return True
        
        return False
    
    def play_game(self):
        print("Welcome to Tic-tac-toe game!")
        
        while True:
            self.board.print_board()
            self.get_move()
            if self.check_winner_or_tie():
                break
            self.switch_player()
            
if __name__ == "__main__":
    game = Game()
    game.play_game()