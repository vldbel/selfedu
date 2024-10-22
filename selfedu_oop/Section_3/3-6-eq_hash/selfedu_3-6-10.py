class Number:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        self.checkvalue(value)
        setattr(instance, self.name, value)

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    @staticmethod
    def checkvalue(val):
        if not isinstance(val, (int, float)) or not (val >= 0):
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = Number()
    b = Number()
    c = Number()

    def __init__(self, a, b, c):
        self.a = a 
        self.b = b
        self.c = c

    @staticmethod
    def checktriange(a, b, c):
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def get_perimeter(self):    
        return self.a + self.b + self.c
    
    def __len__(self):
        return int(self.get_perimeter())
    
    def __call__(self):
        p = self.get_perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    
    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"

    def __setattr__(self, name:str, value):
        if name.startswith("_"):
            # setting value after basic validation
            target_vars = ['_a', '_b', '_c']
            filtered_vars = list(filter(lambda x: x in target_vars, self.__dict__.keys()))
            if len(filtered_vars) >= len(target_vars)-1:
                # we are setting 3rd var or changing one of them = need to check triangle validity
                target_vars.remove(name)
                self.checktriange(value, self.__dict__[target_vars[0]], self.__dict__[target_vars[1]])

        super().__setattr__(name, value)


print("-----------------------------")
tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
 
trf = Triangle(3.4, 4, 5)
print(trf)
# tr.a = 1 
# tr.c = 100