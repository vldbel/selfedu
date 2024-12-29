"""Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str"""

class StringDigit(str):
    def __new__(cls, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return super().__new__(cls, string)

    def __add__(self, other):
        res = super().__add__(other)
        return self.__class__(res)
    
    def __radd__(self, other):
        print(self, other)
        res = other.__add__(self)
        return self.__class__(res)


sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
    
try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"