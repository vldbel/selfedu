class Book:
    def __init__(self, title:str="", author:str="", pages:int=0, year:int=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, name: str, value: any):
        if name in ("title", "author") and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if name in ("pages", "year") and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, name, value)


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
# book = Book(123, "Сергей Балакирев", 123, 2022)
