"""Подвиг 7 (познание срезов)"""

class RadiusVector:
    def __init__(self, *args):
        if not args:
            raise ValueError
        self.coords = list(args)

    def __getitem__(self, idx):
        return tuple(self.coords[idx]) if isinstance(idx, slice) else self.coords[idx]
    
    def __setitem__(self, idx, val):
        self.coords[idx] = val


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5