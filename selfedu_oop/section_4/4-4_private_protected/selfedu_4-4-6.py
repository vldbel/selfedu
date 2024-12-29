"""Подвиг 6. Объявите класс Furniture (мебель)"""

class Furniture:
    def __init__(self, name:str, weight:float):
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        verificators = {'_name': self.__verify_name, '_weight': self.__verify_weight}
        if key in verificators:
            verificators[key](value)
        super().__setattr__(key, value)

    @staticmethod
    def __verify_name(name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(val for key, val in self.__dict__.items() if key.startswith('_'))
    

class Closet(Furniture):
    def __init__(self, name:str, weight:float, tp:bool, doors:int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name:str, weight:float, height:int|float):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name:str, weight:float, height:int|float, square:int|float):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())