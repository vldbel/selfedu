@staticmethod
def list_sub_list(a, b):
     b = [(x, type(x)) for x in b]
     return [x for x in a if (x, type(x)) not in b or b.remove((x, type(x)))]