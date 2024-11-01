class Cell:
    def __init__(self, value):
        self.value = value

class SparseTable:
    def __init__(self):
        self.tbl = {}

    @property
    def rows(self):
        print('here')
        return max(i[0] for i in self.tbl) + 1 if self.tbl else 0

    @property
    def cols(self):
        print('here')
        return max(i[1] for i in self.tbl) + 1 if self.tbl else 0

    def add_data(self, row, col, data):
        self.tbl[row, col] = data

    def remove_data(self, row, col):
        if not (row, col) in self.tbl:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.tbl[row, col]

    def __getitem__(self, key):
        if not key in self.tbl:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.tbl[key].value

    def __setitem__(self, key, v):
        self.tbl.setdefault(key, Cell(0)).value = v

st = SparseTable()
st.add_data(0, 0, "a")
st.add_data(0, 1, "b")
st.add_data(1, 0, "c")
st.add_data(1, 1, "d")
st.remove_data(1, 1)
print(st.rows)
print(st.cols)