class SingletonFive:
    obj_counter = 0
    last_obj = None
    
    def __new__(cls, *args, **kwargs):
        if cls.obj_counter < 5:
            cls.last_obj = super().__new__(cls)
            cls.obj_counter += 1
        return cls.last_obj
                
    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
print(*objs, sep='\n')