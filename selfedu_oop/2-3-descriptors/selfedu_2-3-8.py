class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, obj, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if self.validate_string(value):
            setattr(obj, self.name, value)

    def validate_string(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class PriceValue:
    def __init__(self, max_price):
        self.max_value = max_price
        
    def __set_name__(self, obj, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        if self.validate_price(value):
            setattr(obj, self.name, value)
        
    def validate_price(self, price):
        return type(price) in (int, float) and 0 <= price <= self.max_value
    
    
class Product:    
    name = StringValue(2, 50)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
    price = PriceValue(10000)    # max_value - максимально допустимое значение
    
    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        """добавление товара в магазин (в конец списка goods);"""
        self.goods.append(product)
    
    def remove_product(self, product: Product):
        """удаление товара из магазина (из списка goods)"""
        self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")