from copy import copy


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value
        
    def __str__(self):
        return str(self.data)
    
    
class Stack:
    def __init__(self):
        self.top = self.last = None
    
    def push_back(self, new):
        if type(new) != StackObj:
            print(f"Converting element {new} with type {type(new)} to StackObj") 
            new = StackObj(new)
        # print(f"adding element {new} to the stack")
        if not self.top:
            self.top = self.last = new
            return
        self.last.next = new
        self.last = new

    def get_prev(self):
        if not self.top:
            return
        cur = self.top
        while cur.next != self.last:
            cur = cur.next
        return cur
    
    def pop_back(self):
        if self.top is None: # Empty stack
            return
        if self.top == self.last: # Deleting single element
            res = self.top
            self.top = self.last = None
            return res
        res = self.last
        self.last = self.get_prev()
        self.last.next = None
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
        self.value = self.top
        return self
    
    def __next__(self):
        if self.value:
            res = self.value
            self.value = self.value.next
            return res
        else: 
            raise StopIteration
    
    def show(self):
        print(f"top: {self.top}, last: {self.last}")
        for no, item in enumerate(st, start=1):
            print(f"# {no}: {item.data} (data type: {type(item.data)}), next: {item.next}")

    @staticmethod
    def check_list_type(lst):
        if type(lst) is not list:
            raise TypeError("Operation allowed only with list type")

# so1 = StackObj(1)
# so2 = StackObj("2")
# so3 = StackObj(3)

# st = Stack()
# st.push_back(so1)
# st.push_back(so2)
# st.push_back(so3)
# st.show()
# print(st.pop_back())
# st.show()

# st = st + StackObj("3")
# st += StackObj("4")
# st.show()
# print(st.pop_back())

# st = st * ["5", "6", "7"]
# st.show()

# st *= ["8", "9", "10"]
# st.show()


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']
st += StackObj("225")
st.pop_back()

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1
    
assert i == len(d), "неверное число объектов в стеке"
