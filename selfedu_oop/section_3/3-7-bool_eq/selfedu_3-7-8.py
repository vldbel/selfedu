from random import randint


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__is_open = False
        self.__number = None

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        self.__is_open = val

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, val):
        if not isinstance(val, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = val

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        if not (isinstance(val, int) and 0 <= val <= 8):  # here could be and issue with "near to border" cells
            raise ValueError("недопустимое значение атрибута")
        self.__number = val
    
    def __bool__(self):
        return not self.is_open
     
    def __str__(self):
        # return "X" if not self.__is_open else "B" if self.__is_mine else str(self.__number)
        return "X" if not self.__is_open else "B" if self.__is_mine else str(self.__number)


class GamePole:
    def __new__(cls, *args, **kwargs):
        # singleton
        if not hasattr(cls, '_GamePole__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, n=4, m=6, mines_count=6):
        self.n = n  # rows
        self.m = m  # columns
        self.mines_count = mines_count
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        self.__pole_cells = [[Cell() for y in range(self.m)] for x in range(self.n)]
        self.set_mines()
        self.calculate_around_mines()

    def set_mines(self):
        self.mines = set()
        while len(self.mines) < self.mines_count:
            self.mines.add((randint(0, self.n-1), randint(0, self.m-1)))
        for mcord_y, mcord_x in self.mines:
            self.__pole_cells[mcord_y][mcord_x].is_mine = True

    def calculate_around_mines(self):
        around_idxs = list(((i, j) for i in range(-1, 2) for j in range(-1, 2) if not(i == j == 0)))
        for pos_y in range(self.n):
            for pos_x in range(self.m):
                curren_cell = self.pole[pos_y][pos_x]
                if not curren_cell.is_mine:
                    curren_cell.number = sum((self.pole[pos_y+add_y][pos_x+add_x].is_mine for add_y, add_x in around_idxs \
                        if (0 <= pos_y+add_y < self.n) and (0 <= pos_x+add_x < self.m)))

    def open_cell(self, i, j):
        if i > self.n or j > self.m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True


    def show_pole(self):
        for line in self.__pole_cells:
            for item in line:
                print(item, ' ',end='')
            print()



p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k+i, l+j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1
                
    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"