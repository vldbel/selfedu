"""Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:"""

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point: x = {self._x}, y = {self._y}"


def convet_to_num(val):
    try:
        return int(val)
    except ValueError:
        return float(val)

try:
    inp = input().split()
    x, y = map(convet_to_num, inp)
    pt = Point(x, y)
except:
    pt = Point()
finally:
    print(pt)
