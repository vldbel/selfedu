"""Подвиг 5. В программе объявлены два класса"""

class ShopGenericView:
    """для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);"""
    def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items()])
    
    def __repr__(self):
        return self.__str__()
    

class ShopUserView:
    """для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних классов (не только Book)."""
    def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items() if key != "_id"])
    
    def __repr__(self):
        return self.__str__()


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

# здесь объявляйте классы ShopGenericView и ShopUserView


book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022


book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _title: Python ООП
# _author: Балакирев
# _year: 2022