class TreeObj:
    """для описания вершин и листьев решающего дерева;"""
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None
        
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, obj):
        self.__left = obj
    
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    """для работы с решающим деревом в целом"""
    def __init__(self) -> None:
        pass
    
    @classmethod
    def predict(cls, root, x):
        if x:
            obj:TreeObj = root
            while not obj.value:
                obj = obj.left if x[obj.indx] else obj.right
            return obj.value 
        
    @classmethod
    def add_obj(cls, obj, node:TreeObj=None, left=True):            
        if node is not None and isinstance(node, TreeObj): # part of branches or a leaf
            if left:
                node.left = obj
            else:  # right
                node.right = obj
        return obj
        
                  
root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)


x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
