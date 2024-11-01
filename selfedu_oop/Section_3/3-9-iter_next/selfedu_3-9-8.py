"""Подвиг 8.
Доведем ее функционал до конца. """

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
        return f"(prev: {self.prev.data if self.prev else None}) {self.data} (next: {self.next.data if self.next else None})"


class Stack:
    def __init__(self):
        self.top = self.__last = None
        self.__len = 0
    
    def __len__(self):
        return self.__len
    
    def push_back(self, obj):
        """добавление объекта класса StackObj в конец стека;"""
        self.__len += 1
        if not self.__last: # first element
            self.top = obj
        else:
            self.__last.next = obj
            obj.prev = self.__last
        self.__last = obj

    def push_front(self, obj):
        self.__len += 1
        if not self.top: # first element
            self.top = obj
        else:
            obj.next = self.top
            self.top.prev = obj
            self.top = obj

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
        return obj.data

    def prep_type(self, obj):
        if not isinstance(obj, StackObj):
            obj = StackObj(obj)
        return obj

    def __setitem__(self, idx, val):
        self.__check_idx(idx)
        # get object
        obj = self.traverse(idx)
        obj.data = val

    def __len__(self):
        return self.__len

    def display(self):
        obj = self.top
        while obj:
            print(obj)
            obj = obj.next
    
    def __iter__(self):
        obj = self.top
        while obj:
            yield obj
            obj = obj.next   
                

so1 = StackObj('1')
so2 = StackObj('2')
so3 = StackObj('3')
so4 = StackObj('4')
so5 = StackObj('5')

st = Stack()
st.push_back(so1)
st.push_back(so2)
st.push_back(so3)
st.push_front(so4)
st.push_front(so5)
# st.pop()
# st.display()
# print(len(st))
# print(st[3])
# st[3] = 5
# print(st[3])


for item in st:
    print(item)