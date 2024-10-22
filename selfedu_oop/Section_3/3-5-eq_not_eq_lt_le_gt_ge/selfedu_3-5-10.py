class Box:
    def __init__(self):
        self.items_lst = []

    def add_thing(self, obj):
        """добавление предмета obj (объект другого класса Thing) в ящик;"""
        self.items_lst.append(obj)

    def get_things(self):
        """получение списка объектов ящика."""
        return self.items_lst
    
    def __eq__(self, other):
        """Ящики считаются равными, если одинаково их содержимое 
        (для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика)."""
        for item in self.get_things():
            if other.items_lst.count(item) != 1:
                return False
        return True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    
    def __eq__(self, other):
        """Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass."""
        return self.name.lower() == other.name.lower() and self.mass == other.mass

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)