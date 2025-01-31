"""Значимый подвиг 7. Вам поручается разработать класс TupleData"""
class CellException(Exception):
    """для объектов класса Cell"""


class CellIntegerException(CellException):
    """для объектов класса CellInteger"""


class CellFloatException(CellException):
    """для объектов класса CellFloat"""


class CellStringException(CellException):
    """для объектов класса CellString"""


class Cell:
    _val_type = None 

    def __init__(self):
        self._value = None # Defines expected type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._validate_type(value)
        self._validate_value(value)
        self._value = value

    @classmethod
    def _validate_type(cls, value):
        if type(value) != cls._val_type:
            raise TypeError(f"Value must have {cls._val_type} type")

    def _validate_value(self, value):
        raise NotImplementedError

    # def __str__(self):
    #     return str(self.value)
        
    # def __repr__(self):
    #     return str(self)

class RangeValidator:
    def _validate_value(self, value):
        if not self._min_value <= value <= self._max_value:
            raise self._exception('значение выходит за допустимый диапазон')


class LengthValidator:
    def _validate_value(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise self._exception('длина строки выходит за допустимый диапазон')


class CellInteger(RangeValidator, Cell):
    _val_type = int
    _exception = CellIntegerException

    def __init__(self, min_value, max_value):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value


class CellFloat(RangeValidator, Cell):
    _val_type = float
    _exception = CellFloatException

    def __init__(self, min_value, max_value):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value

class CellString(LengthValidator, Cell):
    _val_type = str
    _exception = CellStringException

    def __init__(self, min_length, max_length):
        super().__init__()
        self._min_length = min_length
        self._max_length = max_length


class TupleData(tuple):
    def __new__(cls, *cells):
        for cell in cells:
            cls._validate(cell)
        return super().__new__(cls, cells)
    
    @staticmethod
    def _validate(val):
        if not isinstance(val, Cell):
            raise TypeError('значения должны иметь тип Cell')

    def _check_idx(self, idx):
        if idx not in range(-len(self), len(self)):
            raise IndexError("Index out of range")

    def __getitem__(self, idx):
        self._check_idx(idx)
        return super().__getitem__(idx).value

    def __setitem__(self, idx, value):
        self._check_idx(idx)
        super().__getitem__(idx).value = value

    def __iter__(self):
        for cell in super().__iter__():
            yield cell.value
    

t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"


cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

    
cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

    
cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(CellStringException, CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"