"""Подвиг 10 (на повторение). 
Объявите класс Matrix (матрица) для операций с матрицами."""

class Matrix:
    def __init__(self, *args):
        # vars set 1 = {"rows": int, "cols": int, "fill_value": (int, float)}
        # vars set 2 = {"list2d": list[list]}

        if len(args) == 3:  # vars set 1
            rows, cols, fill_value = args[0], args[1], args[2]
            self.validate_args1(rows, cols, fill_value)
            self.list2d = [[fill_value for col in range(cols)] for row in range(rows)]
            self.rows, self.cols = rows, cols

        elif len(args) == 1: # vars set 2
            list2d = args[0]
            self.validate_args2(list2d)
            self.list2d = list2d
            self.rows, self.cols = len(self.list2d), len(self.list2d[0]) 
        else:  # unexpected number of vars
            raise KeyError("wrong list of args")
        
    def validate_args1(self, rows, cols, fill_value):
        if not all((
            rows > 0, cols > 0,
            isinstance(rows, int), isinstance(cols, int),
            isinstance(fill_value, (int, float)),
        )):
            raise TypeError('аргументы rows, cols - целые положительные числа; fill_value - произвольное число')

    def validate_args2(self, list2d):
        if not all((
            isinstance(list2d, list), 
            all(len(row) == len(list2d[0]) for row in list2d),
            all(isinstance(cur, int) for line in list2d for cur in line)
            )):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def _check_coords(self, row, col):
        if  not all(map(lambda idx: isinstance(idx, int), (row, col))
            or not -self.rows <= row < self.rows
            or not -self.cols <= col < self.cols):
            raise IndexError('недопустимые значения индексов')
        
    def _check_type(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, coords):
        row, col = coords
        self._check_coords(row, col)
        return self.list2d[row][col]

    def __setitem__(self, coords, val):
        row, col = coords
        self._check_coords(row, col)
        self._check_type(val)
        self.list2d[row][col] = val
    
    @staticmethod
    def _check_mtx_same_size(mtx1, mtx2):
        if len(mtx1.list2d) != len(mtx2.list2d) \
            or len(mtx1.list2d[0]) != len(mtx2.list2d[0]):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if isinstance(other, Matrix):
            self._check_mtx_same_size(self, other)
            return Matrix([[self[row, col] + other[row, col] for col in range(self.cols)] for row in range(self.rows)])
        elif isinstance(other, (int, float)):
            return Matrix([[self[row, col] + other for col in range(self.cols)] for row in range(self.rows)])
            
    def __sub__(self, other):
        if isinstance(other, Matrix):
            self._check_mtx_same_size(self, other)
            return Matrix([[self[row, col] - other[row, col] for col in range(self.cols)] for row in range(self.rows)])
        elif isinstance(other, (int, float)):
            return Matrix([[self[row, col] - other for col in range(self.cols)] for row in range(self.rows)])
    
    def __str__(self):
        return str(self.list2d)

        
list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -6]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"