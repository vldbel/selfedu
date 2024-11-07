class Point:
    def __new__(cls, *args, **kwargs):
        print("Call of __new__ for " + str(cls))
        return super().__new__(cls)
        
        
    def __init__(self, x=0, y=0):
        print("Call of __init__ for " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(str(pt))