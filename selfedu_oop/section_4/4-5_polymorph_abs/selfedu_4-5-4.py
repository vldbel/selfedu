class ShopInterface:
    _id = -1
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
    
    @classmethod
    def _set_id(cls): 
        cls._id += 1
        return cls._id 

class ShopItem(ShopInterface):
    def __init__(self, name:str, weight:int, price:[int, float]):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self._set_id()
        
    def get_id(self):
        return self.__id


item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
print(item1.get_id())
print(item2.get_id())    