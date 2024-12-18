class Protists:
    def __init__(self, name:str, weight:float, old:int):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


# --------------------
class Monkey(Monkeys):
    """наследуется от Monkeys и служит для описания обезьян"""
    pass


class Person(Human):
    """наследуется от Human и служит для описания человека"""
    pass


class Flower(Flowering):
    """наследуется от Flowering и служит для описания цветка;"""
    pass


class Worm(Worms):
    """наследуется от Worms и служит для описания червей."""
    pass


# Создайте в программе следующие объекты и сохраните их в виде списка lst_objs:

lst_objs = [Monkey("мартышка", 30.4, 7), 
            Monkey("шимпанзе", 24.6, 8), 
            Person("Балакирев", 88, 34), 
            Person("Верховный жрец", 67.5, 45), 
            Flower("Тюльпан", 0.2, 1), 
            Flower("Роза", 0.1, 2), 
            Worm("червь", 0.01, 1), 
            Worm("червь 2", 0.02, 1)
            ]

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]  # все объекты, относящиеся к животным (Animals);
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)] # все объекты, относящиеся к растениям (Plants);
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]  # все объекты, относящиеся к млекопитающим (Mammals).

print(lst_animals)
print(lst_plants)
print(lst_mammals)