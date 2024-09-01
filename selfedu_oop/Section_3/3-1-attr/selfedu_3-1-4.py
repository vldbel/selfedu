from typing import Any


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        """- добавление нового товара в магазин (в конец списка goods);"""
        self.goods.append(product)
        
    def remove_product(self, product):
        """- удаление товара product из магазина (из списка goods);"""
        self.goods.remove(product)


class Product:
    id = 0
    
    def __init__(self, name, weight, price):
        self.id = self.get_id()
        self.name = name
        self.weight = weight
        self.price = price
    
    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name in ("name") and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if name in ("price", "weight") and (type(value) != int or value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        
        object.__setattr__(self, name, value)                
    
    def __delattr__(self, name: str) -> None:
        if name == "id":
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id}, {p.name}, {p.weight}, {p.price}")

