from string import ascii_lowercase, digits



# здесь объявляйте классы TextInput и PasswordInput
class Input:
    MIN_NAME_LEN = 3
    MAX_NAME_LEN = 50

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CORRECT_CHARS = CHARS + CHARS.upper() + digits
    
    def __init__(self, name, size=10):
        self.name = name if self.check_name(name) else None
        self.size = size
        
    @classmethod
    def check_name(cls, name):
        if not(cls.MIN_NAME_LEN <= len(name) <= cls.MAX_NAME_LEN)\
            or \
            not (all(char in cls.CORRECT_CHARS for char in name)):
            raise ValueError("некорректное поле name")
        return name

class TextInput(Input):
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Input):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

# inp = TextInput("name", 5)
# print(inp, inp.name, inp.size)