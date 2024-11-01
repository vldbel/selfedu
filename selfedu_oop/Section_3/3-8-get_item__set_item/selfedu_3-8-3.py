"""Подвиг 3. Вам необходимо для навигатора реализовать определение маршрутов. """

class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.route = []

    def add_point(self, x, y, speed):
        self.route.append(((x, y), speed))

    def _check_idx(self, idx):
        if not isinstance(idx, int):
            raise IndexError('некорректный индекс')
        if not(0 <= idx <= len(self.route)-1):
            raise IndexError('некорректный индекс')

    def __getitem__(self, idx):
        self._check_idx(idx)
        return self.route[idx]
    
    def __setitem__(self, idx, val):
        self._check_idx(idx)
        coords, _ = self.route[idx]
        self.route[idx] = (coords, val)


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
c, s = tr[0]
assert c == (20, 0) and s == 100, "Неверно работает add_point"
tr[0] = 120
c, s = tr[0]
assert c == (20, 0) and s == 120, "Неверно работает __getitem__/__setitem__"

tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

try:
    res = tr[3]  # IndexError
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

print('Ok')