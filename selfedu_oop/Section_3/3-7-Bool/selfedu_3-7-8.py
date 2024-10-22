class Cell:
    def __init__(self):
        self.content = None
        self.__is_open = False

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        self.__is_open = val

    def __str__(self):
        pass

class GamePole:
    def __new__(cls):
        # singleton
        if not hasattr(cls, '_GamePole__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, n=4, m=6, mines_count=6):
        self.n = n  # rows
        self.m = m  # columns
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        self.__pole_cells = [[Cell() for y in range(self.m)] for x in range(self.n)]
        # set mines above

    def open_cell(self, i, j):
        self.__pole_cells[i, j].is_open = True


    def show_pole(self):
        for line in self.__pole_cells:
            for item in line:
                cell = '?' if item == None else 'b' if item else '?'
                print(cell, ' ',end='')
            print()



pole = GamePole()
pole.show_pole()