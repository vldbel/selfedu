"""Подвиг 2. Объявите класс Record (запись)"""

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __check_idx(self, idx):
        if not isinstance(idx, int):
            raise IndexError('неверный индекс поля')
        if not (0 <= idx <= len(self.__dict__) - 1):
            raise IndexError('неверный индекс поля')
    

    def __get_key_by_idx(self, idx):
        self.__check_idx(idx)
        return list(self.__dict__.keys())[idx]

    def __getitem__(self, idx):
        key = self.__get_key_by_idx(idx)
        return self.__dict__[key]

    def __setitem__(self, idx, val):
        key = self.__get_key_by_idx(idx)
        self.__dict__[key] = val

r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r.pk)
print(r[0])

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
# r[3] # генерируется исключение IndexError

print(r.__dict__)