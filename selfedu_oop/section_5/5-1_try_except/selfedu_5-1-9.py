"""Подвиг 9. Объявите в программе класс Triangle, объекты которого создаются командой:"""

class Triangle:
    def __init__(self, a, b ,c):
        self._a = a
        self._b = b
        self._c = c

    def __setattr__(self, name, value):
        if name in ("_a", "_b", "_c"):  # we are setting one of triange sides
            self._check_pos_num(value)
            sides = ["_a", "_b", "_c"]
            sides.remove(name)  # get names of other sides of triangle
            side1, side2 = sides
            if hasattr(self, side1) and hasattr(self, side2): # lets check of other sides are set
                self._check_sides(value, getattr(self, side1), getattr(self, side2))
        super().__setattr__(name, value)


    @staticmethod
    def _check_pos_num(val):
        if type(val) not in (int, float) or val <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
    
    @staticmethod
    def _check_sides(*sides):
        for side in sides:
            if sum(sides) - side <= side:
                raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for triangle_sides in input_data:
    try:
        obj = Triangle(*triangle_sides)
        lst_tr.append(obj)
    except (ValueError, TypeError):
        next

# print(lst_tr)