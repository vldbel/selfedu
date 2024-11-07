"""Подвиг 9 (релакс). Объявите в программе класс Bag (сумка)"""

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"{self.name}: {self.weight}"
    

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def check_wigth(self, new_item, exclude=None):
        if sum(thing.weight for idx, thing in enumerate(self.things) if idx != exclude) + new_item.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, item):
        self.check_wigth(item)
        self.things.append(item)

    def __check_idx(func):
        def wrapper(self, idx, *args):
            if idx > len(self.things)-1:
                raise IndexError('неверный индекс')
            return func(self, idx, *args)
        return wrapper

    @__check_idx
    def __getitem__(self, idx):
        return self.things[idx]
    
    @__check_idx
    def __setitem__(self, idx, item):
        self.check_wigth(item, exclude=idx)
        self.things[idx] = item

    @__check_idx
    def __delitem__(self, idx):
        del self.things[idx]

    def __str__(self):
        return f"Overal weight: {self.get_wigth()}.\nList of things: {self.things}"


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"