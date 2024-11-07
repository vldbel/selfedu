class Person:
    types_dict ={
                    "fio": str, 
                    "job": str, 
                    "old": int, 
                    "salary": (float, int), 
                    "year_job": int
                }
    vars_list = dict(enumerate(types_dict))

    def __init__(self, *args):
        if len(args) != len(self.types_dict):
            raise ValueError("wrong args count")

        for idx, arg in enumerate(args):
            key = self.vars_list[idx]
            self.check_val_type(key, arg)
            setattr(self, self.vars_list[idx], arg)
    
    def check_val_type(self, key, val):
        val_type = self.types_dict[key]
        if not isinstance(val, val_type):
            raise TypeError(f"'{val}' stands for '{key}' and must be an obj with type: {val_type.__name__}")

    def check_idx(func):
        def wrapper(self, idx, *args):
            if not isinstance(idx, int) or not (0 <= idx < len(self.vars_list)):
                raise IndexError('неверный индекс')
            return func(self, idx, *args)
        return wrapper

    @check_idx
    def __getitem__(self, idx):
        key = self.vars_list[idx]
        return getattr(self, key)
    
    @check_idx
    def __setitem__(self, idx, val):
        key = self.vars_list[idx]
        self.check_val_type(key, val)
        setattr(self, key, val)


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)

for prop in pers:
    print(prop)
