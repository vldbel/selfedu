"""Подвиг 8. Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". """

class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0
    
    def __bool__(self):
        return self.is_free
    
    def __repr__(self):
        return "-" if self.is_free else "0" if self.value-1 else "X"

class TicTacToe:
    grid_size = 3

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.grid_size)) for _ in range(self.grid_size))

    def clear(self):
        for line in self.pole:
            for cell in line:
                cell.is_free = True
                cell.value = 0

    def __check_idx(self, idx):
        if not (0 <= idx <= self.grid_size-1):
            raise IndexError('неверный индекс клетки')

    def __check_busy(self, row, col):
        if not self.pole[row][col].is_free:
            raise ValueError('клетка уже занята')

    def __setitem__(self, pos, val):
        row, col = pos
        self.__check_idx(row), self.__check_idx(col)
        self.__check_busy(row, col)
        cell = self.pole[row][col]
        cell.value, cell.is_free = val, False

    def __getitem__(self, pos):
        row, col = pos
        # print(f"row: {row}, col: {col}")
        if not isinstance(row, slice) and not isinstance(col, slice):  # single cell
            self.__check_idx(row), self.__check_idx(col)
            return self.pole[row][col].value
        elif isinstance(col, slice):  # horizontal slice
            self.__check_idx(row)
            return tuple(item.value for item in self.pole[row])
        elif isinstance(row, slice):
            self.__check_idx(col)
            return tuple(line[col].value for line in self.pole)

    def display(self):
        for line in self.pole:
            print(line)

g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
 