"""Подвиг 10 (на повторение, релакс). Объявите класс с именем Food (еда)"""

class Food:
    validation_rules = {
            '_name': lambda x: type(x) == str,
            '_weight': lambda x: isinstance(x, (int, float)) and x > 0,
            'calories': lambda x: isinstance(x, int) and x > 0,
            }
    
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories

    def __setattr__(self, key, value):
        if key in self.validation_rules:
            if not self.validation_rules[key](value):
                raise ValueError(f'Invalid value for {key}: {value}')
        super().__setattr__(key, value)

class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white

class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")