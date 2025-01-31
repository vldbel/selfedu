"""Подвиг 8. Объявите класс с именем Rect (прямоугольник)"""

class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, name, value):
        if name in ("_x", "_y", "_width", "_height"):
            self._check_num(value)
        if name in ("_width", "_height"):
            self._check_positive(value)
        super().__setattr__(name, value)

    @staticmethod
    def _check_num(val):
        if type(val) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        
    @staticmethod
    def _check_positive(val):
        if val <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        
    def is_collision(self, rect):
        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or \
            self._y + self._height < self._y or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')
        return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []
for i, obj1 in enumerate(lst_rect):
    try:
        for j, obj2 in enumerate(lst_rect):
            if i != j:
                obj1.is_collision(obj2)
    except TypeError:
        continue
    else:
        lst_not_collision.append(obj1)

print(lst_not_collision)