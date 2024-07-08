class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_coord(self):
        return self.x, self.y
    
v = Vector(1, 2)
res = Vector.get_coord(v)
print(res)