"""Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска),
    объекты которого создаются командой:"""

class Box3D:
    def __init__(self, width:int|float, height:int|float, depth:int|float):
        self.width = width
        self.height = height
        self.depth = depth
    
    def __add__(self, right):
        return Box3D(self.width + right.width, self.height + right.height, self.depth + right.depth)

    def __sub__(self, right):
        return Box3D(self.width - right.width, self.height - right.height, self.depth - right.depth)

    def __mul__(self, right):
        return Box3D(self.width * right, self.height * right, self.depth * right)

    def __rmul__(self, right):
        return self * right

    def __floordiv__(self,right):
        return Box3D(self.width // right, self.height // right, self.depth // right)
    
    def __mod__(self,right):
        return Box3D(self.width % right, self.height % right, self.depth % right)


    def __str__(self):
        return(f"{self.width}, {self.height}, {self.depth}")


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
