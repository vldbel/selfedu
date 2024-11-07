from random import randint

class Cell:
    str = {0: u'\u2b1c', 1: u'\u274c', 2: u'\u2b55'}

    def __init__(self):
        self.value = 0

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other

    def __bool__(self):
        return self.value == 0

    def __repr__(self):
        return self.str[self.value]
    
    def __str__(self):
        return self.__repr__()
    

class TicTacToe:
    POLE_SIZE = 3      # размер поля
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.POLE_SIZE)) for _ in range(self.POLE_SIZE))

    def init(self):
        self.clean_pole()
    
    def clean_pole(self):
        for row in range(self.POLE_SIZE):
            for col in range(self.POLE_SIZE):
                self.pole[row][col].value = self.FREE_CELL
    
    def _check_coords(self, coords):
        if not isinstance(coords, (tuple, list)) or len(coords) != 2:
            raise IndexError('некорректно указанные индексы')
        row , col = coords
        if not isinstance(row, int) or not isinstance(col, int):
            raise IndexError('некорректно указанные индексы')
        if 0 > col >= self.POLE_SIZE or 0 > row >= self.POLE_SIZE:
            raise IndexError('некорректно указанные индексы')
        
    def __getitem__(self, coords):
        self._check_coords(coords)
        row , col = coords
        return self.pole[row][col].value

    def __setitem__(self, coords, val):
        self._check_coords(coords)
        row, col = coords
        if self[row, col] != 0:
            raise ValueError("поле уже занято")
        self.pole[row][col].value = val
    
    def __str__(self):
        out = ''
        for line in self.pole:
            for item in line:
                out += str(item) + ' '
            out += "\n"
        return out

    def show(self):
        print(self) 
        
    def human_go(self):
        while True:
            try:
                row, col = map(int, input("Input coords (format: 'row col'): ").strip().split())
            except:
                print('wrong input')
            else:
                try: 
                    self[row, col] = self.HUMAN_X
                except ValueError:
                    print("поле уже занято, выберите другое")
                    continue
                break

    def _get_free_cell_coords(self):
        free_coords = [(row, col) for row in range(self.POLE_SIZE) for col in range(self.POLE_SIZE) if not self[row, col]]
        return free_coords[randint(0, len(free_coords)-1)]

    def computer_go(self):
        row, col = self._get_free_cell_coords()
        self[row, col] = self.COMPUTER_O

    def _check_win(self, val):
        if any([all(map(lambda x: x == val, line)) for line in self.pole]) \
            or any([all(map(lambda x: x == val, line)) for line in list(zip(*self.pole))]) \
            or all([self[idx, idx] == val for idx in range(self.POLE_SIZE)]) \
            or all([self[idx, self.POLE_SIZE-1-idx] == val for idx in range(self.POLE_SIZE)]):
            return True
        return False
  
    @property
    def is_human_win(self):
        return self._check_win(self.HUMAN_X)
    
    @property
    def is_computer_win(self):
        return self._check_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        st = {item.value for line in self.pole for item in line if item} 
        return not len(st)
            
    def __bool__(self):
        return not self.is_human_win and not self.is_computer_win and not self.is_draw


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
print(game)
print(game.is_human_win, game.is_computer_win, game.is_draw)
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"