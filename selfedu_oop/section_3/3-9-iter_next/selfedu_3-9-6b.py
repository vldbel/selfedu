class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for row in range(len(self.lst)):
            for col in range(row+1):
                # print(f'row: {row}; col: {col}')
                yield self.lst[row][col]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)