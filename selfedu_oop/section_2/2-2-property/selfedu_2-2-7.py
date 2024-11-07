class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    
    def __init__(self, x=0, y=0):
        self.__x = x if self.__check_value(x) else 0
        self.__y = y if self.__check_value(y) else 0
    
    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
    
    @property 
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if self.__check_value(value):
            self.__x = value
            
    @property 
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if self.__check_value(value):
            self.__y = value
    
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y};"
    
    @classmethod
    def __check_value(cls, value):
        if not(type(value) in (int, float)):
            return False
        if not (cls.MIN_COORD <= value <= cls.MAX_COORD):
            return False
        return True
    
    
v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
v4 = RadiusVector2D(-101, 2000)    # радиус-вектор с координатами (1; 2)
