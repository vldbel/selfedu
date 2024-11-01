"""Подвиг 7. 
Необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка."""

class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.line = -1
        return self

    def __next__(self):
        self.line += 1
        if self.line == len(self.lst):
            raise StopIteration
        return self.lst[self.line][self.column]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)