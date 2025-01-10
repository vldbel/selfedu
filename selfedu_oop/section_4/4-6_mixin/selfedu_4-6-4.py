"""Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам."""


class Digit:
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self._validate(value)

    def _validate(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение должно быть числом')
        return value


class Integer(Digit):
    def _validate(self, value):
        super()._validate(value)
        if type(value) != int:
            raise TypeError('число должно быть целым')
        return value
    
class Float(Digit):
#    @staticmethod
    def _validate(self, value):
        super()._validate(value)
        if type(value) != float:
            raise TypeError('число должно быть вещественным')
        return value
    
class Positive(Digit):
    def _validate(self, value):
        super()._validate(value)
        if value <= 0:
            raise TypeError('число должно быть положительным')
        return value

class Negative(Digit):
    def _validate(self, value):
        super()._validate(value)
        if value >= 0:
            raise TypeError('число должно быть отрицательным')
        return value


class PrimeNumber(Integer, Positive):
    ...


class FloatPositive(Float, Positive):
    ...


# Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. 
# Сохраните все эти объекты в виде списка digits.
digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
lst_positive = filter(lambda x: isinstance(x, Positive), digits) # все объекты, относящиеся к классу Positive;
lst_float = filter(lambda x: isinstance(x, Float), digits) # все объекты, относящиеся к классу Float.

print(list(lst_positive))
print(list(lst_float))

test = Digit(1)
print(test)

test = Integer(2)
print(test)

test = Float(3.0)
print(test)

test = Positive(4.0)
print(test)

test = Negative(-5)
print(test)

test = PrimeNumber(6)
print(test)

test = FloatPositive(6.0)
print(test)




# print(digits)