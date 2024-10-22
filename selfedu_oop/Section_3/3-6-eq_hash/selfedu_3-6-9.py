"""Подвиг 9 (релакс)"""

class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ("a", "b", "c"):
            self.check_value(value)
        object.__setattr__(self, key, value)


    @staticmethod
    def check_value(val):
        if not val > 0:
            raise ValueError("габаритные размеры должны быть положительными числами") 
    
    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other) 
    
    def __gt__(self, other):
        return self.__hash__() > other.__hash__()

    def __ge__(self, other):
                return self.__hash__() >= other.__hash__()

    def __str__(self):
         return f"[{self.a}, {self.b}, {self.c}]"

    def __repr__(self):
         return self.__str__()


s_inp = "1 2 3; 4 5 6.78; 1 2 3; 2 1 2.5"
lst_dims = []
for line in s_inp.strip().split("; "):
    data = map(float, line.split())
    lst_dims.append(Dimensions(*data))

lst_dims = sorted(lst_dims, key=lst_dims.__hash__)
print(lst_dims)
for item in lst_dims:
    print(item.__hash__())