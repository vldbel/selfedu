class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next = None
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        self.__prev = obj
 
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj

    def __str__(self):
        return f"{self.data}"

    def __repr__(self) -> str:
         return self.data
    

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.nodes_cnt = 0
         
    def add_obj(self, obj:ObjList):
        """добавление нового объекта obj класса ObjList в конец связного списка;"""
        if not self.head:  # adding the first element
            self.head = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
        self.tail = obj
        self.nodes_cnt += 1
        
    def check_indx(self, indx):
        if indx > self.nodes_cnt - 1:
            raise ValueError("indx is greater than nodes count")
    
    def get_node_by_indx(self, indx):
        self.check_indx(indx)
        link = self.head
        for _ in range(indx):
            link = link.next
        return link
        
    def remove_obj(self, indx): 
        """удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); 
           индекс отсчитывается с нуля."""            
        link = self.get_node_by_indx(indx)
        if not link: return
        if self.head == self.tail:  # We are removing the single element in the list 
            self.head = self.tail = None
        elif link.prev is None: # We are removing the first object
            self.head = self.head.next
            self.head.prev = None
        elif link.next is None:  # we are removing the last object
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # we are removing node in the middle
            link = self.get_node_by_indx(indx)
            # now link is connected to the element to delete
            link.prev.next = link.next
            link.next.prev = link.prev
        self.nodes_cnt -= 1
        
    def __len__(self):
        """возвращает число объектов в связном списке;"""
        return self.nodes_cnt

    def __call__(self, indx):
        """возвращает строку __data, хранящуюся в объекте класса ObjList, 
           расположенного под индексом indx (в связном списке)."""
        link = self.get_node_by_indx(indx)
        return link.data
    
    def __str__(self):
        return ', '.join(self.__repr__())
    
    def __repr__(self):
        link = self.head
        lst = []
        while link:
            lst.append(link.data)
            link = link.next
        return lst
    
        
linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
print(linked_lst(0))
print(linked_lst(1))
print(linked_lst(2))
# print(linked_lst(3))