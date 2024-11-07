class PolyLine:
    def __init__(self, start_coord, *args):
        self.coords = [start_coord] + list(args)
    
    def add_coord(self, x, y):
        """добавление новой координаты (в конец);"""
        self.coords.append((x, y))
    
    def remove_coord(self, indx):
        """удаление координаты по индексу (порядковому номеру, начинается с нуля);"""
        self.coords.pop(indx)
    
    def get_coords(self):
        """получение списка координат (в виде списка из кортежей)."""
        return self.coords
    
    
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(10,10)
print(poly.get_coords())