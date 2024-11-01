"""Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных"""

class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.array = [cell() for _ in range(self.max_length)]

    def _check_idx(func):
        def wrapper(self, *args):
            idx, *values = args
            if not isinstance(idx, int):
                raise IndexError('неверный тип индекса для доступа к элементам массива')
            if not (-self.max_length <= idx < self.max_length):
                raise IndexError('неверный индекс для доступа к элементам массива')
            return func(self, *args)
        return wrapper

    @_check_idx
    def __getitem__(self, idx):
        return self.array[idx].value

    @_check_idx
    def __setitem__(self, idx, val):
        self.array[idx].value = val
    
    def __str__(self):
        return ' '.join(map(str, self.array))

class Num:
    def __init__(self, start_value=0):
        self._value = self.ntype(start_value)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self.check_value(val)
        self._value = val

    def __repr__(self):
        return str(self.value)

    @classmethod
    def check_value(cls, val):
        if not isinstance(val, cls.ntype):
            raise ValueError(f'должно быть целое {cls.ntype}')

class Integer(Num):
    ntype = int


class Float(Num):
    ntype = float
    

a = Array(20, cell=Integer)
assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a = Array(2, cell=Integer)
a[0] = 1
a[1] = 2
assert str(a) == "1 2", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"

try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    a[100] = 25
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"