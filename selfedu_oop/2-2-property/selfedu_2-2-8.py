class TreeObj:
    """для описания вершин и листьев решающего дерева;"""
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None
        
    @property
    def left(self):
        return self.left
    
    @left.setter
    def left(self, obj):
        self.__left = obj
    
    @property
    def right(self):
        return self.right
    
    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    """для работы с решающим деревом в целом"""
    
    @classmethod
    def predict(cls, root, x):
        ...
    
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        ...