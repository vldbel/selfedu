"""Подвиг 6."""

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    def __repr__(self):
        return f"{self.data} ({self.next.data if self.next else None}) ({self.prev.data if self.prev else None})"


class Stack:
    def __init__(self):
        self.top = self.__last = None
        self.__len = 0
    
    def __len__(self):
        return self.__len
    
    def push(self, obj):
        """добавление объекта класса StackObj в конец стека;"""
        self.__len += 1
        if not self.__last: # first element
            self.top = obj
        else:
            self.__last.next = obj
            obj.prev = self.__last
        self.__last = obj
    
        
    def pop(self):
        """извлечение последнего объекта с его удалением из стека;"""
        if not self.__last: # no objects
            return StopIteration
        self.__len -= 1
        res = self.__last
        if self.top == self.__last:  # removing single element    
            self.top = self.__last = None
        else:
            self.__last = self.__last.prev
            self.__last.next = None
        return res

    def __check_idx(self, idx):
        if not (-self.__len <= idx < self.__len):
            raise IndexError('неверный индекс')

    def traverse(self, idx):
        obj = self.top
        for _ in range(idx):
            obj = obj.next
        return obj

    def __getitem__(self, idx):
        self.__check_idx(idx)
        obj = self.traverse(idx)
        return obj 

    def prep_type(self, obj):
        if not isinstance(obj, StackObj):
            obj = StackObj(obj)
        return obj

    def __setitem__(self, idx, val):
        self.__check_idx(idx)
        # prepare new object
        new_st_obj = self.prep_type(val)
        # get object to replace
        old_st_obj = self.traverse(idx)
        # relinking chain
        if old_st_obj.prev:
            old_st_obj.prev.next = new_st_obj
        if old_st_obj.next:
            old_st_obj.next.prev = new_st_obj
        new_st_obj.next = old_st_obj.next
        new_st_obj.prev = old_st_obj.prev

    
    def display(self):
        obj = self.top
        while obj:
            print(obj)
            obj = obj.next
                

# el1 = StackObj("first")
# el2 = StackObj("second")
# el3 = StackObj("third")
# el4 = StackObj("fourth")
# el5 = StackObj("fifth")
# print(el1, el2, el3, el4, el5)

# stack = Stack()
# stack.push(el1)
# stack.push(el2)
# stack.push(el3)
# stack.push(el4)
# stack.push(el5)
# stack.pop()
# print("--------")
# print(stack[0])
# print(stack[1])
# print(stack[2])
# print(stack[3])
# print("--------")
# stack[2] = 'third-replaced'
# stack.display()
# print("--------")
# stack[0] = 'first-replaced'
# stack[3] = 'last-replaced'
# stack.display()
# print("--------+")
# for item in stack:
#     print(item.data)

st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next
    
assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"