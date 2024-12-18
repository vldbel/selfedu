"""Подвиг 4. Разрабатывается интернет-магазин. """

class Thing:
    def __init__(self, name:str, price:int, weight:int):
        self.name, self.price, self.weight = name, price, weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))
    

class DictShop(dict):
    def __init__(self, dct=None):
        if not (dct is None or isinstance(dct, dict)):
            raise TypeError('аргумент должен быть словарем')
        super().__init__({self._check_key(key): val for key, val in dct.items()} if dct else {})

    def __setitem__(self, key, val):
        super().__setitem__(self._check_key(key), val)

    @staticmethod
    def _check_key(key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return key
    

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)
