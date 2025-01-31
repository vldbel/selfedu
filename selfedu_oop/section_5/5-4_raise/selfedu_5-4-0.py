class MyCustomException(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.details = args[1]
    
    def __str__(self):
        return f"Ошибка: {self.message}, детали: {self.details}"
    

raise MyCustomException("Test Message", "Test details")