# здесь объявляется класс Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def clone(self):
        return Point(self.x, self.y)

pt = Point(2, 3)
print(pt)
pt_clone = pt.clone()
print(pt_clone)