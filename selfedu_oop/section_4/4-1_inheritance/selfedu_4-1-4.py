"""Подвиг 4. Наследование часто используют"""

class Animal:
    def __init__(self, name:str, old:int):
        self.name = name
        self.old = old

    def get_info(self):
        return f"{self.name}: {self.old}, " + ', '.join(list(map(str, self.__dict__.values()))[2:])

class Cat(Animal):
    def __init__(self, name:str, old:int, color:str, weight:int|float):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

class Dog(Animal):
    def __init__(self, name:str, old:int, breed:str, size:tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size


cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())