"""Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел."""

class ListInteger(list):
    _allowed_types = (int, )

    def _check_value(self, value):
        if not isinstance(value, self._allowed_types):
            raise TypeError('можно передавать только целочисленные значения')
        return value

    def __init__(self, values=None):
        super().__init__(map(self._check_value, values) if values is not None else [])

    def __setitem__(self, idx, value):
        super().__setitem__(idx, self._check_value(value))

    def append(self, value):
        super().append(self._check_value(value))


s = ListInteger((1, 2, 3))
x = ListInteger()
print(x)
print(s)
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError