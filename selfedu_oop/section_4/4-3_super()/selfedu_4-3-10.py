"""Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs"""

class ItemAttrs:
    def __getitem__(self, key):
        return self.coords[key]

    def __setitem__(self, key, val):
        self.coords[key] = val


class Point(ItemAttrs):
    def __init__(self, *coords):
        self.coords = list(coords)


pt = Point(1, 2.5)
print(pt.__dict__)

x = pt[0]   # 1
y = pt[1]   # 2.5
print(x, y)
pt[0] = 10
print(pt.__dict__)
