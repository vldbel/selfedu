class StackObj:
    """для описания объектов односвязного списка;"""
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def __str__(self):
        return self.data
        
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj
    
    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, data):
        self.__data = data
        
           
class Stack: 
    """для управления односвязным списком."""
    def __init__(self):
        self.top = None

    def __get_last_stackobj(self):
        pointer = self.top
        while pointer.next:
            pointer = pointer.next
        return pointer

    def push(self, obj:StackObj): 
        """добавление объекта класса StackObj в конец односвязного списка;"""
        if not self.top:  # first element
            self.top = obj
            return
        last = self.__get_last_stackobj()
        last.next = obj 

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка;"""
        if not self.top: # no elements in the list
            return
        
        if not self.top.next: # last element
            last_obj = self.top
            self.top = None
            return last_obj
        
        # more than 2 elements in the list
        current = self.top
        while current.next: # while next node exists
            prev = current
            current = current.next # switcheing to the next node
        # here are: 'current' must be the last element in the list, 'prev' - previous to the last
        prev.next = None
        return current
        
    def get_data(self):
        """получение списка из объектов односвязного списка (список из строк локального атрибута 
        __data каждого объекта в порядке их добавления, или пустой список, если объектов нет)."""
        full_data_list = []
        if self.top:
            pointer = self.top
            while pointer:
                full_data_list.append(pointer.data)
                pointer = pointer.next
        return full_data_list
        


st = Stack()

st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
res = st.pop()
print(res)

res = st.get_data()    # ['obj1', 'obj2']
print(f"List content: {res}")
