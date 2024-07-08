from random import randint 

MAX_MINE_RATIO = 0.25

class Cell:
    def __init__(self, around_mines=None, is_mine=False):
        self.around_mines = around_mines
        self.is_mine = is_mine
        self.fl_open = False
    
    def __str__(self):
        return "#" if not self.fl_open else "X" if self.is_mine else str(self.around_mines)
        

class GamePole:
    def __init__(self, size, mines_cnt):
        self.size = size
        if mines_cnt > (size**2 * MAX_MINE_RATIO):
            raise ValueError(f"Number of Mines must be not more than total cells count * {MAX_MINE_RATIO})")
        self.mines_cnt = mines_cnt
        self.init()

    def init(self):
        self.generate_pole_template()
        self.generate_mines()
        self.set_mines()
        self.calculate_around_mines()
    
    def generate_pole_template(self):
        self.pole = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
    
    def generate_mines(self):
        self.mines = set()
        while len(self.mines) < self.mines_cnt:
            mine_pos_y = randint(0, self.size-1)
            mine_pos_x = randint(0, self.size-1)
            self.mines.add((mine_pos_y, mine_pos_x))

    def set_mines(self):
        for mine in self.mines:
            mine_pos_y, mine_pos_x = mine
            self.pole[mine_pos_y][mine_pos_x].is_mine = True
    
    def calculate_around_mines(self):
        around_idxs = list(((i, j) for i in range(-1, 2) for j in range(-1, 2) if not(i == j == 0)))
        for pos_y in range(self.size):
            for pos_x in range(self.size):
                curren_cell: Cell = self.pole[pos_y][pos_x]
                if not curren_cell.is_mine:
                    curren_cell.around_mines = sum((self.pole[pos_y+add_y][pos_x+add_x].is_mine for add_y, add_x in around_idxs \
                        if (0 <= pos_y+add_y < self.size) and (0 <= pos_x+add_x < self.size)))
    
    def open_cell(self, y_pos, x_pos):
        self.pole[y_pos][x_pos].fl_open = True
        return "X" if self.pole[y_pos][x_pos].is_mine else None
                
    def show(self):
        for y_pos in range(self.size):
            for x_pos in range(self.size):
                print(self.pole[y_pos][x_pos], end="  ")
            print()

def play():
    size = 10
    mines = 12
    pole_game = GamePole(size, mines)    
    # while True:        
    #     pole_game.show()
    #     if pole_game.open_cell(*user_input()) == "X":
    #         pole_game.show()
    #         print("BOOM!") 
    #         exit()
        
            
def user_input():
    y, x = map(int, input("Select cell to open: row, column: ").split(","))
    return y, x

    
if __name__ == "__main__":
    play()