"""Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:"""

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, width, height, depth):
        self.__a = width
        self.__b = height
        self.__c = depth

    @classmethod
    def check_coord(cls, val):
        return cls.MIN_DIMENSION <= val <= cls.MAX_DIMENSION
            
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, val):
        if self.check_coord(val):
            self.__a = val 

    @b.setter
    def b(self, val):
        if self.check_coord(val):
            self.__b = val 

    @c.setter
    def c(self, val):
        if self.check_coord(val):
            self.__c = val 

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __eq__(self, other):
        return self.volume == other.a * other.b * other.c

    def __gt__(self, other):
        return self.volume > other.a * other.b * other.c
    
    def __ge__(self, other):
        return self.volume >= other.a * other.b * other.c
    
    def __repr__(self):
        return f"width: {self.a}, height: {self.b}, depth: {self.c}"


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name  # название товара;
        self.price = price # цена товара;
        self.dim = dim  # габариты товара (объект класса Dimensions).

    def __repr__(self):
        return f"Name: {self.name}, price: {self.price}, dimensions: [{self.dim}], volume: {self.dim.volume}"


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim.volume)


# assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

# lst_sp = []
# lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
# lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
# lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
# lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

# lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
# s = [x.name for x in lst_shop_sorted]
# assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)

assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10

print(d1)
print(d2)
print(d3)
# assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"
