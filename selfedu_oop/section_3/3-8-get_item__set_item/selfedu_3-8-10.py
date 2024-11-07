"""Подвиг 10. Необходимо описывать в программе очень большие и разреженные таблицы данных"""

class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.table = {}

    def _update_row_col_after_add(self, coord):
        row, col = coord
        if self.rows-1 < row:  # update rows if new item has bigger row
            self.rows = row + 1 
        if self.cols-1 < col:  # update rows if new item has bigger col
            self.cols = col + 1

    def _update_row_col_after_delete(self, row, col):
        if row == self.rows - 1:  # rescan only if we deleted element with max val of row
            self.rows = max(row for row, _ in self.table) + 1
        if col == self.cols - 1:  # rescan only if we deleted element with max val of col
            self.cols = max(col for _, col in self.table) + 1

    def _check_exists(self, coord):
        if coord not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')

    def _check_coords(self, coord):
        if coord not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self._update_row_col_after_add((row, col))

    def remove_data(self, row, col):
        self._check_exists((row, col))
        self.table.pop((row, col))
        self._update_row_col_after_delete(row, col)
    
    def __getitem__(self, coord):
        self._check_coords(coord)
        return self.table[coord].value
    
    def __setitem__(self, coord, val):
        self.table.setdefault(coord, Cell(val)).value = val
        self._update_row_col_after_add(coord)


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"