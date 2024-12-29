"""Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list."""

class SoftList(list):
    def __getitem__(self, key):
        return super().__getitem__(key) if self.__check_idx__(key) else False
    
    def __setitem__(self, key, val):
        return super().__setitem__(key, val) if self.__check_idx__(key) else False
    
    def __check_idx__(self, idx):
        return idx in range(-len(self), len(self))


sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(len(sl))
print(sl[6]) # False
print(sl[-7]) # False
