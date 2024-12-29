"""Подвиг 5. Объявите класс Animal (животное)"""

class Animal:
    def __init__(self, name:str, kind:str, old:int):
        self.__name =  name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property 
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, val):
        self._kind = val

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, val):
        self.__old = val


animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3) ]