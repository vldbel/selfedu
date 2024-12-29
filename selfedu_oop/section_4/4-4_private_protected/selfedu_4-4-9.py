"""Подвиг 9 (на повторение). Функцию-декоратор class_log"""

vector_log = []

def class_log(log:list):
    def wrapper_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_method(v))
        return cls
    
    def log_method(func):
        def wrapper(*args, **kwargs):
            log.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return wrapper_methods
 
@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)