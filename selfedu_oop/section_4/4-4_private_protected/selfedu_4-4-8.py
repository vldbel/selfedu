"""Подвиг 8. Объявите базовый класс Aircraft (самолет)"""

class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, name, value):
        if name in ("_model", ):
            if type(value) != str:
                raise TypeError('неверный тип аргумента')
        if name in ("_mass", "_speed", "_top"):
            if type(value) not in (int, float):
                raise TypeError('неверный тип аргумента')
            if value <= 0:
                raise TypeError('неверный тип аргумента')
            
        if name in ("_chairs", ):
            if type(value) not in (int, ):
                raise TypeError('неверный тип аргумента')
            if value <= 0:
                raise TypeError('неверный тип аргумента')

        if name in ("_weapons", ):
            if type(value) != dict:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(name, value)

    
class PassengerAircraft(Aircraft):
    """пассажирский самолет"""
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs  # chairs - число пассажирских мест (целое положительное число)

class WarPlane(Aircraft):
    """военный самолет"""
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons  # weapons - вооружение (словарь); ключи - название оружия, значение - количество


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
    ]

air = Aircraft('model', 1, 2, 3)
assert air._model == 'model' and air._mass == 1 and air._speed == 2 and air._top == 3, "неверные значения атрибутов объекта класса Aircraft"


try:
    air = Aircraft('4', 1, -2, 3)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды Aircraft('4', 1, -2, 3)"

try:
    PassengerAircraft('model', 1, 2, 3, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды PassengerAircraft('model', 1, 2, 3, 0)"


try:
    WarPlane('model', 1, 2, 3, [1, 2])
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды WarPlane('model', 1, 2, 3, [1, 2])"