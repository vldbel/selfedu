import sys

# здесь пишите программу
class Book:
    def __init__(self, title, author, pages):
        """где  title - название книги (строка); 
                author - автор книги (строка); 
                pages - число страниц в книге (целое число)."""
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"

lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)

book = Book(*lst_in) 
print(book)