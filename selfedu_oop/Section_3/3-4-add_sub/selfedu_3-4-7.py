"""Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). """


class Book:
    """Book - для описания отдельной книги"""
    def __init__(self, title:str, author:str, year:int):
        """title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число)."""
        self.title = title
        self.author = author
        self.year = year


class Lib:
    """Lib - для представления библиотеки в целом"""
    def __init__(self):
        self.book_list = []

    def __add__(self, right):
        self.book_list.append(right)
        return self

    def __sub__(self, right):
        if isinstance(right, Book):
            self.book_list.remove(right)
        else:
            self.book_list.pop(right)
        return self

    def __len__(self):
        return len(self.book_list)
