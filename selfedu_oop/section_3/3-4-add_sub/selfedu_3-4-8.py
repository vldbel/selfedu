"""Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два класса с именами:"""

class Item:
    """пункт расходов бюджета"""
    def __init__(self, name, money):
        """где name - название статьи расхода; money - сумма расходов (вещественное или целое число)."""
        self.name = name
        self.money = money
    
    def __add__(self, right):
        return self.money + right.money if isinstance(right, Item) else self.money + right
    
    def __radd__(self, left):
        return self + left
    

class Budget:
    """для управления семейным бюджетом;"""
    def __init__(self):
        self.lst = []

    def add_item(self, it):
        """добавление статьи расхода в бюджет (it - объект класса Item);"""
        self.lst.append(it)

    def remove_item(self, indx):
        """удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);"""    
        self.lst.pop(indx)

    def get_items(self):
        """"возвращает список всех статей расходов (список из объектов класса Item)."""
        return self.lst


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
