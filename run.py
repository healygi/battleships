from random import randint

print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
greeting = "Welcome to Battleships- play against the computer and be the first to sink all 5 of your opponent's ships."
print(greeting)
#ask for players name
name = input("What is your name Comrade? " )
print("Hello " + name )
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("lets set out to sea and destroy the computers ships!!")
print("Instructions: Board size- 8. Number of ships- 5. Top left corner is row: 0, column: 0.")
print("LETS PLAY!")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

class Board(object):
    size_x = 8
    size_y = 8
    ships_number = 5
    empty_symbol = "*"
    ship_symbol = "0"
    values = []
    label = ""
    hit = "X"

    def __init__(self, label):
        self.values = []
        self.label = label

    def generate(self):
        for row in range(0, self.size_y):
            columns = []
            for column in range(0, self.size_x):
                columns.append(self.empty_symbol)
            self.values.append(columns)
    
    def print(self, hidden=True):
        print("    " + self.label + " Board")
        print("=====================")
        for row in self.values:
            formated_row = " ".join(row)
            formated_row = "== " + formated_row + " =="
            if hidden:
                formated_row = formated_row.replace(self.ship_symbol, self.empty_symbol) 
            print(formated_row)
        print("=====================")

    def place_ships_auto(self):
        ships_placed = 0
        while ships_placed < self.ships_number:
            random_x = randint(0, self.size_x - 1)
            random_y = randint(0, self.size_y - 1)
            # TODO validate space is empty
            self.values[random_x][random_y] = self.ship_symbol
            ships_placed = ships_placed + 1

    def guess_is_valid(self, guess_x, guess_y):
        try:
            x = int(guess_x)
            y = int(guess_y)
            if (x <= self.size_x and y <= self.size_y) and (x>0 and y>0):
                return True
            else:
                print('Coordinates outside the board, please enter again')
                return False
        except:
            print('Please enter a integer number')
            return False

    def user_guess(self, pc_board):
        input_valid = False
        while input_valid is False:
            x = input(f'Row [0 - {self.size_x}]: ')
            y = input(f'Column [0 - {self.size_y}]: ')
            input_valid = self.guess_is_valid(x, y)
        self.attack_board(int(x), int(y), pc_board)

        """
        if statment to check if guess is a hit or not. Attack
        method for computer and user to attack board
        """
    
    def attack_board(self, x, y, opponent_board):
        print(f'Attacking {opponent_board.values[x][y]}')
        print(f'opponent board position is: ${opponent_board.values[x][y]}')
        print(f'ship symbol is: ${self.ship_symbol}')
        if opponent_board.values[x][y] == self.ship_symbol:
            print("HIT!")
            opponent_board.values[x][y] == "X"
            #self.update_user_board(x, y, opponent_board)
        else:
            print("MISS!")
        """
    def update_user_board(self, x, y, opponent_board):
        shot = opponent_board.values[x][y]
        if shot == self.ship_symbol:
            self.ship_symbol[x][y] = self.hit[x][y]
        """

    def pc_guess(self, user_board):
        input_valid = False
        while input_valid is False:
            x = randint(0, 8 -1)
            y = randint(0, 8 -1)
            input_valid = self.guess_is_valid(x, y)
        print("Computers turn to attack")
        print("Shots fired....")
        self.attack_board(int(x), int(y), user_board)
        print(f'computer guess:[{int(x)} , {int(y)}]')
    
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                 hit_ships += 1
        return hit_ships

def run_game(pc_board, user_board):
    pc_board.user_guess(pc_board)
    user_board.pc_guess(user_board)
    turns = 10
    while turns > 0:
        user_board.user_guess(pc_board)
        pc_board.pc_guess(user_board)
        turns -= 1

        #checks if duplicate guess
        # while user_guess.pc_board[int(x)][int(y)] == "-" or user_guess.pc_board[int(x)][int(y)]== "X":
        #     print("You guessed that one already")
        #     x, y = Board.user_guess(object)
        #     #check for hit or miss
        # if user_guess.attack_board.values[int(x)][int(y)] == "X":
        #     print("You sunk 1 of my battleships!")
        #     user_guess.pc_board[int(x)][int(y)]= "X"
        # else:
        #     print("MISS!")
        #     user_guess.pc_board[int(x)][int(y)] = "-"
        #     #check if win or lose
        # if Board.count_hit_ships(pc_board) == 5:
        #     print("PC hit all 5 of your battleships!")
        # elif Board.count_hit_ships(user_board) == 5:
        #     print("You hit all 5 battleships!")
        #     break
        # else:
        #     turns -= 1
        #     print(f"You have {turns} turns remaining")
        #     if turns == 0:
        #      print("Sorry you ran out of turns")
        #      user_board(user_guess)
        #      break   

if __name__ == "__main__":
    pc_board = Board("PC")
    pc_board.generate()
    pc_board.place_ships_auto()
    pc_board.print(False)
    user_board = Board(name.capitalize() + "'s")
    user_board.generate()
    user_board.place_ships_auto()
    user_board.print(False)
    run_game(pc_board, user_board)