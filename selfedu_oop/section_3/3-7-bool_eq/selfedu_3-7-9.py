"""Подвиг 9 (на повторение)."""

class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("vector must not be empy")
        self.coords = list(args)
    
    def __str__(self):
        return str(self.coords) 

    def __len__(self):
        return len(self.coords)
    
    @staticmethod
    def compare_length(a, b):
        if len(a) != len(b):
            raise ArithmeticError('размерности векторов не совпадают')
        
    def __add__(self, other):
        self.compare_length(self, other)
        return Vector(*(i + j for i, j in zip(self.coords, other.coords)))

    def __sub__(self, other):
        self.compare_length(self, other)
        return Vector(*(i - j for i, j in zip(self.coords, other.coords)))
    
    def __mul__(self, other):
        self.compare_length(self, other)
        return Vector(*(i * j for i, j in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            coords = [other] * len(self)
        elif isinstance(other, Vector):
            self.compare_length(self, other)
            coords = other.coords
        else:
            raise ValueError('type not allowed')
        for idx, _ in enumerate(self.coords):
            self.coords[idx] += coords[idx]
        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            coords = [other] * len(self)
        elif isinstance(other, Vector):
            self.compare_length(self, other)
            coords = other.coords
        else:
            raise ValueError('type not allowed')
        for idx, _ in enumerate(self.coords):
            self.coords[idx] -= coords[idx]
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            coords = [other] * len(self)
        elif isinstance(other, Vector):
            self.compare_length(self, other)
            coords = other.coords
        else:
            raise ValueError('type not allowed')
        for idx, _ in enumerate(self.coords):
            self.coords[idx] *= coords[idx]
        return self

    def __eq__(self, other):
        # self.compare_length(self, other)
        return len(self) == len(other) and all([x == y for x, y in zip(self.coords, other.coords)])

# vector_1 = Vector(1, 2, 3)
# vector_2 = Vector(4, 5, 6)
# print(vector_1 + vector_2)
# print(vector_2 - vector_1)
# print(vector_1 * vector_2)
# vector_1 += 10
# print(vector_1)
# vector_2 -= 1
# print(vector_2)
# print(vector_1 == vector_2)
# print(vector_1 != vector_2)


vector_1 = Vector(1, 2, 3)
vector_2 = Vector(4, 5, 6)
vector_2_1 = Vector(4, 5, 6, 7)
assert vector_1 != vector_2, "Вектора vector_1(1, 2, 3) и vector_2(3, 4, 5) должны быть не равны"
assert vector_2 != vector_2_1, "Вектора vector_2(4, 5, 6) и vector_2_1(4, 5, 6, 7) должны быть не равны"

vector_3 = Vector(1, 2, 3)
assert vector_1 == vector_3, "Вектора vector_1(1, 2, 3) и vector_3(1, 2, 3) должны быть равны"

id_vector_1 = id(vector_1)
id_vector_2 = id(vector_2)
vector_1_add_2 = vector_1 + vector_2
assert id_vector_1 != id(vector_1_add_2), "При сложение Векторов должен создаваться новый объект."
assert vector_1_add_2.coords == [5, 7, 9], "Неверно работает сложение векторов."

vector_1_sub_2 = vector_1 - vector_2
assert id_vector_1 != id(vector_1_sub_2), "При вычитании Векторов должен создаваться новый объект."
assert vector_1_sub_2.coords == [-3, -3, -3], "Неверно работает вычитание векторов."

vector_1_mul_2 = vector_1 * vector_2
assert id_vector_1 != id(vector_1_mul_2), "При умножении Векторов должен создаваться новый объект."
assert vector_1_mul_2.coords == [4, 10, 18], "Неверно работает умножение векторов."

id_vector_1_str = str(id(vector_1))
vector_1 += 10
assert id_vector_1_str == str(
    id(vector_1)), "При сложении вектора с числом (vector_1 += 10), новый объект создаваться не должен"
assert vector_1.coords == [11, 12, 13], "Неверно работает сложение вектора с числом (vector_1 += 10)"

vector_1 -= 10
assert id_vector_1_str == str(
    id(vector_1)), "При вычитании числа из вектора (vector_1 -= 10), новый объект создаваться не должен"
assert vector_1.coords == [1, 2, 3], "Неверно работает вычитание числа из вектора (vector_1 -= 10)"

vector_1 *= 10
assert id_vector_1_str == str(
    id(vector_1)), "При умножении вектора на число (vector_1 *= 10), новый объект создаваться не должен"
assert vector_1.coords == [10, 20, 30], "Неверно работает умножение вектора на число (vector_1 *= 10)"

vector_2_2 = Vector(10, 10, 10)
vector_1 += vector_2_2
assert id_vector_1_str == str(
    id(vector_1)), "При сложении векторор (vector_1 += vector_2_2), новый объект создаваться не должен"
assert vector_1.coords == [20, 30, 40], "Неверно работает сложение векторов (vector_1 += vector_2_2)"

vector_1 -= vector_2_2
assert id_vector_1_str == str(
    id(vector_1)), "При вычитании векторов (vector_1 -= vector_2_2), новый объект создаваться не должен"
assert vector_1.coords == [10, 20, 30], "Неверно работает вычитание векторов (vector_1 -= vector_2_2)"

vector_1 *= vector_2_2
assert id_vector_1_str == str(
    id(vector_1)), "При умножении векторов (vector_1 *= vector_2_2), новый объект создаваться не должен"
assert vector_1.coords == [100, 200, 300], "Неверно работает умножение векторов (vector_1 *= vector_2_2)"

vector_add = Vector(1, 1, 1, 1)
try:
    vector_1 = vector_1 + vector_add
except ArithmeticError:
    assert True
else:
    assert False, "при сложении векторов (vector_1 = vector_1 + vector_add) не сгенерировалось исключение ArithmeticError"""

try:
    vector_1 += vector_add
except ArithmeticError:
    assert True
else:
    assert False, "при сложении векторов (vector_1 += vector_add) не сгенерировалось исключение ArithmeticError"""

vector_sub = Vector(1, 1, 1, 1)
try:
    vector_1 = vector_1 - vector_sub
except ArithmeticError:
    assert True
else:
    assert False, "при вычитании векторов (vector_1 = vector_1 - vector_sub) не сгенерировалось исключение ArithmeticError"""

try:
    vector_1 -= vector_sub
except ArithmeticError:
    assert True
else:
    assert False, "при вычитании векторов (vector_1 -= vector_sub) не сгенерировалось исключение ArithmeticError"""

vector_mul = Vector(1, 1, 1, 1)
try:
    vector_1 = vector_1 * vector_mul
except ArithmeticError:
    assert True
else:
    assert False, "при умножении векторов (vector_1 = vector_1 * vector_mul) не сгенерировалось исключение ArithmeticError"""

print("Отлично")