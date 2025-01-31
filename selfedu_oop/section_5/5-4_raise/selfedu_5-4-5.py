"""Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError"""

class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
    
    def __str__(self):
        if hasattr(self, "id"):
            return f"Значение первичного ключа id = {getattr(self, 'id')} недопустимо"
        if hasattr(self, "pk"):
            return f"Значение первичного ключа pk = {getattr(self, 'pk')} недопустимо"
        else:
            return "Первичный ключ должен быть целым неотрицательным числом"


e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо

try:
    raise PrimaryKeyError(id = -10.5)
except Exception as e:
    print(e)