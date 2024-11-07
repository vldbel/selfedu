from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True
    

class LengthValidator:
    """для проверки длины данных в диапазоне [min_length; max_length];"""
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        
    def __call__(self, string):
        return self.min_length <= len(string) <= self.max_length

class CharsValidator:
    """для проверки допустимых символов в строке."""
    def __init__(self, charset):
        self.charset = charset
        
    def __call__(self, string):
        set(string)
        return set(string).issubset(set(self.charset))


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
    
lv = LengthValidator(5, 10) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator("12345") # chars - строка из допустимых символов

res = lv("12345")
print(res)
res = cv("123")
print(res)