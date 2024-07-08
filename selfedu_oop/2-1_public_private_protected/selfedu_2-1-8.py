class  Point:
    def __init__(self, x, y):
        if all(map(lambda x: type(x) in (int, float), (x, y))):
            self.__x = x
            self.__y = y
        
    def get_coords(self):
        return self.__x, self.__y
    
    def __str__(self):
        return str(f"{self.__x}, {self.__y}")


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4 and all(map(lambda x: type(x) in (int, float), args)):
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)
        else:
            raise ValueError()
            
        # __sp - объект класса Point с координатами x1, y1 (верхний левый угол);
        # __ep - объект класса Point с координатами x2, y2 (нижний правый угол).
        
    def set_coords(self, sp:Point, ep:Point):
        self.__sp = sp
        self.__ep = ep
        
    def get_coords(self):
        return self.__sp, self.__ep
    
    def draw(self):
        print(f"Прямоугольник с координатами: ({self.__sp}), ({self.__ep})")
    
    
pt = Point(1, 2)
print(pt)

r1 = Rectangle(Point(0, 0), Point(20, 34))
r1.draw()
r2 = Rectangle(10, 10, 20, 20)
r2.draw()