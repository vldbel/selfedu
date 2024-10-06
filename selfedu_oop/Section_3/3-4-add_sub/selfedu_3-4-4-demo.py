class NewList:
    def __init__(self, lst:list=None):
        self._lst = lst.copy() if lst and type(lst) == list else []
        
    def get_list(self):
        return self._lst

    def __sub__(self, other: list or NewList):
        if type(other) not in (list, self.__class__):
            raise ArithmeticError("Right operand must be a list or NewList object")
        
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))
    
    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Right operand must be a list or NewList object")
        return NewList(self.__diff_list(other, self._lst))
    
    @staticmethod
    def __is_elem(item, sub:list):
        res = any(map(lambda x: type(item) == type(x) and item == x, sub))
        if res:
            sub.remove(item)
        return res
    
    @staticmethod
    def __diff_list(lst_1 :list, lst_2 :list):
        if not len(lst_2):
            return lst_1
        sub = lst_2.copy()
        return [x for x in lst_1 if not NewList.__is_elem(x, sub)]
    
    
lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]