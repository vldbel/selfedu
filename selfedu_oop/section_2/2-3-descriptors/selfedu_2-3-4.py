class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1.5, 2.3)
pt.__dict__['x'] = 10.0
print(pt.x)