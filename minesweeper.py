import random

class Minesweeper:
    def __init__(self, row = 5, col = 5):
        self.beaten = False
        self.lost = False
        self.n_correct_cells = 0
        self.play_field = [['-' for x in range(col)] for y in range(row)]
        self.generate_solution_field(row, col)
    
    def is_beaten(self):
        return self.beaten
    
    def generate_solution_field(self, row, col):
        self.solution_field = [[0 for x in range(col)] for y in range(row)]
        for x in range(len(self.solution_field)):
            for y in range(len(self.solution_field[x])):
                random_num = random.randint(1, 100)
                if random_num <= 20:
                    self.solution_field[x][y] = "X"
                    
                    
        for x in range(len(self.solution_field)):
            for y in range(len(self.solution_field[x])):
                if self.solution_field[x][y] != "X":
                    n_mines = 0
                    if x > 0:
                        if self.solution_field[x - 1][y] == "X":
                            n_mines += 1
                            
                    if x < len(self.solution_field) - 1:
                        if self.solution_field[x + 1][y] == "X":
                            n_mines += 1
                    
                    if x > 0 and y < len(self.solution_field[x]) - 1:
                        if self.solution_field[x - 1][y + 1] == "X":
                            n_mines += 1
                        
                    if x < len(self.solution_field) - 1 and y < len(self.solution_field[x]) - 1:
                        if self.solution_field[x + 1][y + 1] == "X":
                            n_mines += 1
                    
                    if x > 0 and y > 0:        
                        if self.solution_field[x - 1][y - 1] == "X":
                            n_mines += 1
                    
                    if x < len(self.solution_field) - 1 and y > 0:
                        if self.solution_field[x + 1][y - 1] == "X":
                            n_mines += 1
                    
                    if y > 0:        
                        if self.solution_field[x][y - 1] == "X":
                            n_mines += 1
                    
                    if y < len(self.solution_field[x]) - 1:
                        if self.solution_field[x][y + 1] == "X":
                            n_mines += 1
                            
                    self.solution_field[x][y] = n_mines
                                                                               
    def pretty_print_solution(self):
        for x in range(len(self.solution_field)):
            for y in range(len(self.solution_field[x])):
                print(self.solution_field[x][y], end=" ")
            print()
            
    def pretty_print_hidden(self):
        for x in range(len(self.play_field)):
            for y in range(len(self.play_field[x])):
                print(self.play_field[x][y], end=" ")
            print()
    
    def set_cell(self, row, col, value=None):
        if value == None:
            self.play_field[row][col] = self.solution_field[row][col]
        else:
            self.play_field[row][col] = "?"
                
    def get_width(self):
        return len(self.solution_field)
    
    def get_height(self):
        return len(self.solution_field[0])
    
    def check_lose(self, row, col):
        if self.play_field[row][col] == "X":
            self.lost = True
            
    def is_lost(self):
        return self.lost
    
    def check_correctness(self, row, col):
        if self.play_field[row][col] == self.solution_field[row][col]:
            self.n_correct_cells += 1
            return True
        
        elif self.play_field[row][col] == "?" and self.solution_field[row][col] == "X":
            self.n_correct_cells += 1
            return True
        return False    
    def check_zero(self, row, col):
        return self.solution_field[row][col] == 0
    
    def open_new_area(self, row, col, expand_left=True, expand_right=True, expand_up=True, expand_down=True):
        if row < self.get_height() and col < self.get_height() and row >= 0 and col >= 0:
            if self.play_field[row][col] != 0 or self.solution_field[row][col] != "X":
                self.play_field[row][col] = self.solution_field[row][col]
                if self.check_zero(row, col):
                    if col < self.get_height() - 1 and expand_right:
                        self.open_new_area(row, col + 1, expand_left=False)
                    if col > 0 and expand_left:
                        self.open_new_area(row, col - 1, expand_right=False)
                    if row < self.get_width() - 1 and expand_down:
                        self.open_new_area(row + 1, col, expand_up=False)
                    if row > 0 and expand_up:
                        self.open_new_area(row - 1, col, expand_down=False)
                    if row < self.get_width() - 1 and col < self.get_height() - 1 and expand_down and expand_right:
                        self.open_new_area(row + 1, col + 1, expand_up=False, expand_right=False)
                    if row < self.get_width() - 1 and col > 0 and expand_down and expand_left:
                        self.open_new_area(row + 1, col - 1, expand_up=False, expand_left=False)
                    if row > 0 and col < self.get_height() - 1 and expand_up and expand_right:
                        self.open_new_area(row - 1, col + 1, expand_down=False, expand_right=False)
                    if row > 0 and col > 0 and expand_up and expand_left:
                        self.open_new_area(row - 1, col - 1, expand_down=False, expand_left=False)
                else:
                    pass
        
        
    def get_n_cells(self):
        return self.get_height() * self.get_height()
        
    def check_win(self):
        if self.n_correct_cells == self.get_n_cells():
            self.beaten = True
        
        return self.beaten
    
            
                         
def parse_input(user_input):
    user_input = user_input.split(" ")
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])
    return user_input

if __name__ == "__main__":
    game = Minesweeper(5, 5)
    while (not game.is_beaten() and not game.is_lost()):
        game.pretty_print_hidden()
        print()
        # game.pretty_print_solution()
        row = 0
        col = 0
        invalid_input = True
        while invalid_input:
            row, col, flag_input = parse_input(input("Please enter row and col: "))
            if row < game.get_width() and col < game.get_height() and row >= 0 and col >= 0:
                invalid_input = False
        
        if not flag_input:
            game.set_cell(row, col)
            game.check_lose(row, col)
            if (not game.is_lost()):
                if game.check_correctness(row, col):
                    if game.check_zero(row, col):
                        game.open_new_area(row, col)
                game.check_win()
        else:
            game.set_cell(row, col, "?")
            game.check_correctness(row, col)
            game.check_win()
            
        
    if game.is_lost():
        print("You have stepped into a mine")   
        
    elif game.is_beaten():
        print("You have won")
