"""Подвиг 9 (на повторение). Вам поручают разработать класс для представления маршрутов в навигаторе. """

class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = self._check_coord_type(val)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = self._check_coord_type(val)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


    @staticmethod
    def _check_coord_type(val):
        if type(val) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return val


class Track:
    def __init__(self, *args):
        if all(map(lambda x: isinstance(x, PointTrack), args)) and len(args) > 0:
            self.__points = list(args)
        elif len(args) == 2:
            self.__points = [PointTrack(*args)]
        else: 
            raise ValueError('wrong track format')

    @property
    def points(self):
        return tuple(self.__points) 

    def add_back(self, pt):
        """добавление новой точки в конец маршрута (pt - объект класса PointTrack);"""
        self.__points.append(pt)

    def add_front(self, pt):
        """добавление новой точки в начало маршрута (pt - объект класса PointTrack);"""
        self.__points.insert(0, pt)

    def pop_back(self):
        """удаление последней точки из маршрута;"""
        return self.__points.pop()

    def pop_front(self):
        """удаление первой точки из маршрута."""
        return self.__points.pop(0)


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)


import pytest


class PointTrack:
    pass

class Track:
    pass


@pytest.mark.parametrize('arguments', [
    (15, -12.3),
    (PointTrack(0.23, -54), PointTrack(-1, 101),),
    (PointTrack(0.23, -54),),
])
def test_track_class_structure(arguments):
    assert hasattr(Track, "points")
    assert type(getattr(Track, "points")) is property
    assert hasattr(Track, 'add_back')
    assert callable(getattr(Track, 'add_back'))
    assert hasattr(Track, 'add_front')
    assert callable(getattr(Track, 'add_front'))
    assert hasattr(Track, 'pop_back')
    assert callable(getattr(Track, 'pop_back'))
    assert hasattr(Track, 'pop_front')
    assert callable(getattr(Track, 'pop_front'))

    tr = Track(*arguments)
    assert hasattr(tr, "points")
    assert type(getattr(tr, "points")) is tuple

def test_point_track_class_structure():
    pt = PointTrack(-12, 22.43)
    assert hasattr(pt, 'x')
    assert hasattr(pt, 'y')
    with pytest.raises(TypeError) as ex:
        pt_error = PointTrack(-11, [22, 4, 7])
    assert 'координаты должны быть числами' in str(ex.value)
    assert str(pt) == f"PointTrack: -12, 22.43"