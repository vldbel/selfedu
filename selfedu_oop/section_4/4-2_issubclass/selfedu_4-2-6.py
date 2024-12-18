"""Подвиг 6. Известно, что с объектами класса tuple """

class Tuple(tuple):
    def __add__(self, other):
        return Tuple(tuple(self) + tuple(other))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"