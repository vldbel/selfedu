class RadiusVector:
    def __init__(self, arg0, *args):
        if len(args) == 0:
            self.__coords = (0,) * arg0
        else:
            self.__coords = (arg0, ) + args
        
    def set_coords(self, *args):
        """для изменения координат радиус-вектора;"""
        if len(args) >= len(self.__coords):
            self.__coords = args[:len(self.__coords)]
        else:
            self.__coords = args + self.__coords[len(args):]
        
    def get_coords(self):
        """для получения текущих координат радиус-вектора (в виде кортежа)."""
        return self.__coords
        
    def __len__(self):
        """возвращает число координат радиус-вектора (его размерность);"""
        return len(self.__coords)
    
    def __abs__(self):
        """возвращает длину радиус-вектора""" 
        return sum(map(lambda x: x**2, self.__coords))**0.5


# создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
# print(vector.get_coords())
# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
vector = RadiusVector(1, -5, 3.4, 10) 
# print(vector.get_coords())


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
# print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
# print(a, b, c)
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
# print(vector3D.get_coords())
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)