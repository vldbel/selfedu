class IterColumn:
    def __init__(self, lst, col_indx):
        self.lst = lst
        self.col_indx = col_indx

    def __iter__(self):
        for row in self.lst:
            yield row[self.col_indx]

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)