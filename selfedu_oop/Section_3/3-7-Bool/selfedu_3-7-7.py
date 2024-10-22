"""Подвиг 7. Объявите класс Ellipse (эллипс),"""

class Ellipse:
    coords_lst = ("x1", "y1", "x2", "y2")
    def __init__(self, *args):
        if len(args) == 4 and all(map(lambda x: isinstance(x, (int, float)), args)):
            for coord, arg in zip(self.coords_lst, args):
                setattr(self, coord, arg)

    def __len__(self):
        return sum(map(lambda x: x in self.coords_lst, self.__dict__)) == 4

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2) 
        

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(1, 1, 2, 2)

lst_geom = [el1, el1, el2, el2]
lst_get_coords = [el for el in lst_geom if el]
# print(lst_get_coords)
