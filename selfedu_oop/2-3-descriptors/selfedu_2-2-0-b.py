class Point3d:
    
    class Integer:
        def __set_name__(self, owner, name):
            self.name = "_" + name
            # print(f"self: {self}, owner: {owner}, name: {name}")
    
        def __get__(self, instance, owner):
            return getattr(instance, self.name)
        
        def __set__(self, instance, value):
            self.verify_coord(value)
            setattr(instance, self.name, value)
        
        @classmethod
        def verify_coord(cls, coord):
            if type(coord) != int:
                raise TypeError("Coord isn't integer")
        
                     
    x = Integer()
    y = Integer()
    z = Integer()


    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
        

def test():
    p = Point3d(1, 2, 1)
    print(f"p: {p}")
    print(f"p.dict: {p.__dict__}")
    # print(f"p type: {type(p._x)}")

if __name__ == "__main__":
    test()