class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    
    def __init__(self, val_a, val_b, val_c):
        self.a = val_a
        self.b = val_b
        self.c = val_c
        
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value
    
    def __setattr__(self, name: str, value) -> None:
        # print('setattr: ', name, value)
        if name in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        
        if name in ('a', 'b', 'c') and not (self.MIN_DIMENSION <= value <= self.MAX_DIMENSION):
            return False
        
        super().__setattr__(name, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError