from typing import Any


class Point:
    MIN_COORD = 0
    MAX_COORD = 100
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
    
    @classmethod        
    def set_bound(cls, left):
        cls.MIN_COORD = left
    
    def __getattribute__(self, name):
        print(f'__getattribute__: item: {name}')
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        print(f"__setattr__: {name}: {value}")
        object.__setattr__(self, name, value)
        
        
    
pt1 = Point(1, 2)
pt2 = Point(10, 20)
a = pt1.x
print(a)