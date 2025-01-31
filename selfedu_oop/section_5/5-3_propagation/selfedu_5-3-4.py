"""Подвиг 4. Объявите класс с именем ValidatorString, объекты которого создаются командой:"""

class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars
    
    def is_valid(self, string):
        is_good = True
        if not (self.min_length <= len(string) <= self.max_length):
            is_good = False
        if self.chars:
            if not any([char in string for char in self.chars]):
                is_good = False
        if not is_good:
            raise ValueError('недопустимая строка')
        return True
    

class LoginForm:
    def __init__(self, login_validator:ValidatorString, password_validator:ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if not ("login" in request and "password" in request):
            raise TypeError('в запросе отсутствует логин или пароль')
        self.login_validator.is_valid(request["login"])
        self.password_validator.is_valid(request["password"])

        self._login = request["login"]
        self._password = request["password"]


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
