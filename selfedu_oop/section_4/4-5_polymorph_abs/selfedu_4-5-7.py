"""Подвиг 7. Используя модуль abc объявите базовый класс с именем StackInterface"""

from abc import ABC, abstractmethod
from copy import copy


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека;"""

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека."""


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value
        
    def __str__(self):
        return str(self.data)
    
    
class Stack(StackInterface):
    def __init__(self):
        self._top = self._last = None
    
    def push_back(self, new):
        if type(new) != StackObj:
            print(f"Converting element {new} with type {type(new)} to StackObj") 
            new = StackObj(new)
        # print(f"adding element {new} to the stack")
        if not self._top:
            self._top = self._last = new
            return
        self._last.next = new
        self._last = new

    def get_prev(self):
        if not self._top:
            return
        cur = self._top
        while cur.next != self._last:
            cur = cur.next
        return cur
    
    def pop_back(self):
        if self._top is None: # Empty stack
            return
        if self._top == self._last: # Deleting single element
            res = self._top
            self._top = self._last = None
            return res
        res = self._last
        self._last = self.get_prev()
        self._last.next = None
        return res
    
    def __add__(self, right):
        new_obj = copy(self)
        if type(right) != StackObj:
            right = StackObj(right) 
        new_obj.push_back(right)
        return new_obj

    def __iadd__(self, right):
        if type(right) != StackObj:
            right = StackObj(right) 
        self.push_back(right)
        return self

    def __mul__(self, right):
        new_obj = copy(self)
        self.check_list_type(right)
        for item in right:
            new_obj.push_back(StackObj(item))
        return new_obj
    
    def __imul__(self, right):
        self.check_list_type(right )
        for item in right:
            self.push_back(StackObj(item))
        return self
    
    def __iter__(self):
        self.value = self._top
        return self
    
    def __next__(self):
        if self.value:
            res = self.value
            self.value = self.value.next
            return res
        else: 
            raise StopIteration
    
    def show(self):
        print(f"top: {self._top}, last: {self._last}")
        for no, item in enumerate(st, start=1):
            print(f"# {no}: {item.data} (data type: {type(item.data)}), next: {item.next}")

    @staticmethod
    def check_list_type(lst):
        if type(lst) is not list:
            raise TypeError("Operation allowed only with list type")


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"