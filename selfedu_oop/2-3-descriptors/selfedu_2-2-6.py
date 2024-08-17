class FloatValue:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        self._check_value(value)
        setattr(obj, self.name, value)
    
    def __delete__(self, obj):
        setattr(obj, self.name, 0)
    
    @classmethod
    def _check_value(cls, val):
        if type(val) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    
class Cell:
    value = FloatValue()
    
    def __init__(self, val=0.0):
        self.value = val
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
        
        
class TableSheet:
    def __init__(self, n, m):
        # n = rows, m = columns
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]
       
    def __str__(self):
        table_repr = ""
        for row in self.cells:
            table_repr += (str(row) + "\n")
        return table_repr


def test():
    table_size = {"n": 5, "m": 3}
    ts = TableSheet(**table_size)
    # print(ts)
    
    val = 1.0
    for n in range(table_size["n"]):
        for m in range(table_size["m"]):
            ts.cells[n][m].value = val
            val += 1
    
    print(ts)
    
    # ts.cells[0][0].value = 'a'
    print(ts.cells[0][0].value)
    print(type(ts.cells[0][0]))
    
if __name__ == "__main__":
    test()