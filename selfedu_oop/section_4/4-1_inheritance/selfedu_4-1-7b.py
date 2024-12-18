"""Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами)"""

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("__new__:", cls)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        print(cls.__instance)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__: 
            self.name = name
        

obj1 = Game("a")

print(obj1.__dict__)

obj2 = Game("b")
print(obj2.__dict__)
