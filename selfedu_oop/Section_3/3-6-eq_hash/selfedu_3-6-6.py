"""Подвиг 6. Объявите класс с именем ShopItem"""

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        """чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;"""
        return hash((self.name.lower(), self.weight, self.price))
    
    def __eq__(self, other):
        return hash(self) == hash(other)
        """чтобы объекты с одинаковыми хэшами были равны."""
    
    def __str__(self):
        return f"{self.name} : {self.weight}, {self.price}"
    
    def __repr__(self):
        return self.__str__()

# it1 = ShopItem("mylo", 0.1, 100)
# it2 = ShopItem("mylo", 0.1, 100)
# print(it1 == it2)
# print(it1, it2, sep='\n')
# print(hash(it1), hash(it2), sep='\n')

lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

# lst_in = list(map(str.strip, sys.stdin.readlines()))

items = [ShopItem(line.split(':')[0], *map(float, line.split(':')[1].split())) for line in lst_in]
# print(items)

shop_items = {}
for item in items:
    if item not in shop_items:
        shop_items[item] = [item, 1]
    else:
        cur = shop_items[item]
        cur[1] += 1
        shop_items[item] = cur
print(shop_items)