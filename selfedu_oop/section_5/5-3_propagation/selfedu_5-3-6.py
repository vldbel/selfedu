"""Подвиг 6. В программе выполняется считывание числовых данных из входного потока"""

class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        cls._check_int(max_length)
        obj = super().__new__(cls, cls._check_length(lst, max_length))
        return obj

    @staticmethod
    def _check_int(val):
        if type(val) != int or val < 0:
             raise TypeError('max length must be positive integer')
        return val

    @staticmethod
    def _check_length(lst, max_length):
        if len(lst) > max_length:
                raise ValueError('число элементов коллекции превышает заданный предел')
        return lst

    def __str__(self):
        return ' '.join([str(item) for item in self])
    
    def __repr__(self):
        return self.__str__()

try:
    digits = list(map(float, input().split()))
    tl = TupleLimit(digits, max_length=5)
except Exception as e:
     print(e)
else: 
     print(tl)
