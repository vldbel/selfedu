class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        if not self.validate(x) or not self.validate(y):
            raise ValueError(f"{x} or {y} not in range ({self.MIN_COORD} to {self.MAX_COORD})")
        self.x = x
        self.y = y

           
    def get_coord(self):
        return self.x, self.y
    
v = Vector(-1, 2)
print(v.get_coord())

