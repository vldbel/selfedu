"""Подвиг 6. 
Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков"""

class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.line = 0
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor+=1
        if self.cursor > self.line:
            self.cursor = 0
            self.line += 1
        if self.line > len(self.lst)-1:
            raise StopIteration
        return self.lst[self.line][self.cursor]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)