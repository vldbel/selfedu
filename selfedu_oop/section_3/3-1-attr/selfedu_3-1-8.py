class Circle:
    __check_values = {"x": (int, float), "y": (int, float), "radius": (int, float)}
    
    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None  # some bullshit here
        self.x = x
        self.y = y
        self.radius = radius
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    
    def __setattr__(self, name: str, value):
        # print('setter: ', name, value)
        if name in self.__check_values and type(value) not in self.__check_values[name]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if name == "radius" and value <= 0: # f"_{self.__class__.__name__}__radius"
            return
        super().__setattr__(name, value)

    def __getattr__(self, name: str):
        return False
    

circle = Circle(10.5, 7, -22)
# print(circle)
# print(circle.__dict__)
print(circle.x, circle.y, circle.radius)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
print(circle.radius)
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
# print(res)