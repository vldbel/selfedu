"""Module dockstring"""

class ListMath:
    """Test class"""
    LIST_ALLOWED_TYPES = [int, float]

    def __init__(self, inlst=None):
        # self.lst_math = self.filter_types(lst) if lst and type(lst) == list else []
        if not inlst:
            self.lst_math = []
        else:
            self.lst_math = self.filter_types(inlst)

    @classmethod
    def filter_types(cls, l:list):
        """check that items in list are in LIST_ALLOWED_TYPES"""
        return [item for item in l if type(item) in cls.LIST_ALLOWED_TYPES]

    @classmethod
    def check_value_type(cls, value):
        """chehcs if value in cls.LIST_ALLOWED_TYPES"""        
        if type(value) not in cls.LIST_ALLOWED_TYPES:
            raise ArithmeticError("Not allowed value")
        return True

    def __str__(self) -> str:
        return str(self.lst_math)

    def __add__(self, item):
        self.check_value_type(item)
        return self.__class__(map(lambda x: x + item, self.lst_math))

    def __radd__(self, item):
        return self.__add__(item)

    def __iadd__(self, item):
        for i, _ in enumerate(self.lst_math):
            self.lst_math[i] += item
        return self

    def __sub__(self, item):
        self.check_value_type(item)
        return self.__class__(map(lambda x: x - item, self.lst_math))

    def __rsub__(self, item):
        self.check_value_type(item)
        return self.__class__(map(lambda x: item - x, self.lst_math))

    def __isub__(self, item):
        for i, _ in enumerate(self.lst_math):
            self.lst_math[i] -= item
        return self

    def __mul__(self, item):
        self.check_value_type(item)
        return self.__class__(map(lambda x: x * item, self.lst_math))

    def __rmul__(self, item):
        return self.__mul__(item)

    def __imul__(self, item):
        for i, _ in enumerate(self.lst_math):
            self.lst_math[i] *= item
        return self

    def __truediv__(self, item):
        self.check_value_type(item)
        return self.__class__(map(lambda x: x / item, self.lst_math))

    def __rtruediv__(self, item):
        return self.__class__(map(lambda x: item / x, self.lst_math))

    def __itruediv__(self, item):
        for i, _ in enumerate(self.lst_math):
            self.lst_math[i] /= item
        return self


lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]

# +
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst)

# -
lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst)
lst = 7.0 - lst # вычитание из числа каждого числа списка
print(lst)
lst -= 76.3
print(lst)

# *
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54

# /
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
