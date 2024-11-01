"""Подвиг 9. 
В программе необходимо реализовать таблицу TableValues"""

class Cell:
    def __init__(self, data):
        self.__data = data
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, val):
        self.__data = val

    def __repr__(self):
        return str(self.data)


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(self.type_data()) for _ in range(cols)] for _ in range(rows)]
        
    def _check_type(self, val):
        if not isinstance(val, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def _check_coord(self, row, col):
        if any((
                not all(map(lambda idx: isinstance(idx, int), (row, col))),
                not(-self.cols <= col < self.cols),
                not(-self.rows <= row < self.rows),
            )):
            raise IndexError('неверный индекс')
        
    def __getitem__(self, coord):
        row, col = coord
        self._check_coord(row, col)
        return self.table[row][col].data

    def __setitem__(self, coord, val):
        self._check_type(val)
        row, col = coord
        self._check_coord(row, col)
        self.table[row][col].data = val

    def __iter__(self):
        for row in self.table:
            yield (item.data for item in row)
            

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
        
assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
 

