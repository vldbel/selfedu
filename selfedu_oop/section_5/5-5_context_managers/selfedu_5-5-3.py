"""Подвиг 3. Объявите класс PrimaryKey"""

class PrimaryKey:
    def __enter__(self):
        print('вход')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type)
        return True


with PrimaryKey() as pk:
    raise ValueError('error message')
