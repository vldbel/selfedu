"""Подвиг 8 (на повторение). В программе объявлен базовый класс Function (функция) следующим образом:"""

class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('амплитуда должна быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj        


class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        self._k, self._b = (args[0], args[1]) if len(args) == 2 else (args[0]._k, args[0]._b)
                    
    def _get_function(self, x):
        return self._k * x + self._b
        
         
f = Linear(1, 0.5)
print(f.__dict__)

f2 = f + 10   # изменение смещения (атрибут _bias)
print(f2.__dict__)

y1 = f(0)     # 0.5
print(y1)

y2 = f2(0)    # 10.5
print(y2)

f = Linear(1, 0.5)
f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
y1 = f(0)     # 0.5
print(y1)
y2 = f2(0)    # 2.5
print(y2)