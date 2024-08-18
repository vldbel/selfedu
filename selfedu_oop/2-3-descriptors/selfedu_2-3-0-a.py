class Point3d:
    def __init__(self, x , y, z):
        self._x = x
        self._y = y
        self._z = z
    
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Coord isn't integer")
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord
        
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord
        

def test():
    p = Point3d(1, 2, 3)
    print(p.__dict__)


if __name__ == '__main__':
    test()