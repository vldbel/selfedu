"""Подвиг 9 (на повторение). Объявите класс IteratorAttrs для перебора всех локальных атрибутов объектов класса. """

class IteratorAttrs:
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key, value)


class SmartPhone(IteratorAttrs):
    def __init__(self, model:str, size:tuple[int, int], memory:int):
        self.model, self.size, self.memory = model, size, memory


phone = SmartPhone("samsung x10", (10, 5), 64)

for attr, value in phone:
    print(attr, value)
