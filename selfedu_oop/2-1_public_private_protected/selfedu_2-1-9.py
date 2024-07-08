class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next  = None
        
    def set_next(self, obj):
        self.__next = obj
        
    def set_prev(self, obj):
        self.__prev = obj
        
    def get_next(self):
        return self.__next
    
    def get_prev(self):
        return self.__prev
    
    def set_data(self, data):
        self.__data = data;
    
    def get_data(self):
        return self.__data
    
    def __str__(self):
        return f"Node data: {self.get_data()};"

class LinkedList:
    def __init__(self):
        self.head:ObjList = None
        self.tail:ObjList = None
        
    def add_obj(self, obj:ObjList):
        if not self.head: # first element
            self.head = obj
            self.tail = self.head
            return
        obj.set_prev(self.tail)
        self.tail.set_next(obj)
        self.tail = obj
        
    def remove_obj(self):
        if not self.tail: # Empty list
            raise ValueError("No elements in the list. Nothing to delete")
            return
        if self.tail == self.head: # Deleting last element
            self.head = self.tail = None
            return
        prev:ObjList = self.tail.get_prev()
        prev.set_next(None)
        self.tail.set_next(None)
        self.tail = prev

    def get_data(self):
        pointer = self.head
        full_data_list = []
        while pointer:
            full_data_list.append(pointer.get_data())
            pointer = pointer.get_next()
        return full_data_list
        
        
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
# print(lst.head)
# print(lst.head.get_next().get_next().get_next())
# print(lst.tail.get_prev().get_prev().get_prev())


res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)