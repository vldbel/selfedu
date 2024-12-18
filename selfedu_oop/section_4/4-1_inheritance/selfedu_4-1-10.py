class Vector:
    _allowed_types = (int, float)

    def __init__(self, *coords):
        self.__check_coords(coords)
        self._coords = coords

    def __check_coords(self, coords):
        if not all(map(lambda x: isinstance(x, self._allowed_types), coords)):
            raise ValueError('координаты должны быть числами')

    def get_coords(self):
        return tuple(self._coords)

    @staticmethod
    def __is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError('операции возможны только с объектами класса вектор')

    def __check_len(self, other):
        if len(self._coords) != len(other._coords):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)
            

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_len(other)
        coords = tuple(x + y for x, y in zip(self._coords, other._coords))
        return self.__make_vector(coords)
    
    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_len(other)
        coords = tuple(x - y for x, y in zip(self._coords, other._coords))
        return self.__make_vector(coords)


class VectorInt(Vector):
    _allowed_types = (int, )


# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# print(v.get_coords())

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')