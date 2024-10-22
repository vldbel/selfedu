"""Подвиг 8."""

class BookStudy:
    def __init__(self, name:str, author:str, year:int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))
    
    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return f"{self.name}, {self.author}, {self.year}"
    
    def __repr__(self):
        return self.__str__()


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []
for line in lst_in:
    data = line.split(";")
    lst_bs.append(BookStudy(data[0], data[1], int(data[2])))

# print(lst_bs)
unique_books = len(set(lst_bs))
# print(unique_books)