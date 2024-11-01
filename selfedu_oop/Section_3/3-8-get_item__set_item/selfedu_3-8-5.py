"""Большой подвиг 5. 
Вам необходимо написать программу для удобного обращения с таблицами однотипных данных """

class IntegerValue:
    """дескриптор данных для работы с целыми числами."""
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

    @classmethod
    def check_value(cls, val):
        if not isinstance(val, int):
            raise ValueError('возможны только целочисленные значения')


class CellInteger:
    """описывает одну ячейку таблицы для работы с целыми числами"""
    value = IntegerValue()  # объект дескриптора, класса IntegerValue.
    
    def __init__(self, start_value=0):
        self.value = start_value

    def __repr__(self):
        return str(self.value)

class TableValues:
    """для работы с таблицей в целом;"""
    def __init__(self, rows, cols, cell):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.check_pos_int(rows), self.check_pos_int(cols)
        self.rows, self.cols = rows, cols
        self.cells = tuple(tuple(cell() for c in range(cols)) for _ in range(rows))

    @classmethod
    def check_pos_int(cls, val):
        if not (isinstance(val, int) and val > 0):
            raise ValueError('кол-во колонок и столбцов должно быть положительныи целым числом')

    def _check_coord(func):
        def wrapper(self, *args):
            (row, col), *vals = args
            if not all(map(lambda x: isinstance(x, int), (row, col))):
                raise ValueError("coords must be an integgers")
            if not (-self.rows-1 <= row <= self.rows) or not(-self.cols-1 <= col <= self.cols):
                raise ValueError('row/col index is out of range')
            return func(self, *args)
        return wrapper
            
    @_check_coord
    def __getitem__(self, coord):
        row, col = coord
        return self.cells[row][col].value

    @_check_coord
    def __setitem__(self, coord, val):
        row, col = coord
        self.cells[row][col].value = val

    def __repr__(self):
        res = ""
        for line in self.cells:
            res = res + (' '.join(map(str, line)))
            if line != self.cells[-1]:
                res += '\n'
        return res


tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
tb[1, 1] = 2
print(tb)
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"