class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length
        
class StringValue:
    def __init__(self, validator):
        self.validator = validator
    
    def __set_name__(self, obj, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        # print(f"set: {obj, self.name, value}")
        if self.validator.validate(value):
            setattr(obj, self.name, value)
                
    
class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())
    
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        """возвращает список из значений полей в порядке [login, password, email]"""
        return [self.login, self.password, self.email]
    
    def show(self):
        """выводит в консоль многострочную строку в формате"""
        print(f"<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>")


form = RegisterForm("login", "password", "email")
print(form.get_fields())
print(form.show())
