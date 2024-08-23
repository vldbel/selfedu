class Book:
    def __init__(self, author, title, price):
        self.set_author(author)
        self.set_title(title)
        self.set_price(price)
    
    def set_title(self, title):
        """Запись в локальное приватное свойство __title объектов класса Book значения title"""
        self.__title = title
        
    def set_author(self, author):
        """Запись в локальное приватное свойство __author объектов класса Book значения author"""
        self.__author = author
        
    def set_price(self, price):
        """запись в локальное приватное свойство __price объектов класса Book значения price"""
        self.__price = price
    
    def get_title(self):
        """получение значения локального приватного свойства __title объектов класса Book"""
        return self.__title
    
    def get_author(self):
        """получение значения локального приватного свойства __author объектов класса Book"""
        return self.__author
    
    def get_price(self):
        """получение значения локального приватного свойства __price объектов класса Book"""
        return self.__price