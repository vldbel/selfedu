class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    @property
    def real(self):
        """для считывания действительного значения;"""
        return self.__real

    @real.setter
    def real(self, value):
        """для записи действительного значения;"""
        self.check_value(value)
        self.__real = value
    
    @property
    def img(self):
        """для считывания мнимого значения."""
        return self.__img

    @img.setter
    def img(self, value):
        """для записи мнимого значения;"""
        self.check_value(value)
        self.__img = value
    
    @classmethod
    def check_value(cls, value):
        ALLOWED_TYPES = [int, float]
        if type(value) not in ALLOWED_TYPES:
            raise ValueError("Неверный тип данных.")
    
    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5
        
cmp  = Complex(7, 8)
cmp.real = 3 
cmp.img = 4
c_abs = abs(cmp)
# print(c_abs) # 5.0