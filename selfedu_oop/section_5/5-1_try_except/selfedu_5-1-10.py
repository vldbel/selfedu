"""Подвиг 10. Объявите в программе класс FloatValidator, объекты которого создаются командой:"""

class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        return self._validate(value)

    def _validate(self, val):
        raise NotImplementedError


class FloatValidator(Validator): 
    def _validate(self, val):
        if type(val) != float:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value <= val <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        return val


class IntegerValidator(Validator):
    def _validate(self, val):
        if type(val) != int:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value <= val <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        return val


def is_valid(lst, validators):
    lst_out = []
    for item in lst:
        for val in validators:
            try:
                print(item, val)
                lst_out.append(val(item))
                break
            except ValueError:
                next
    return lst_out


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)