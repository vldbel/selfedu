from string import ascii_letters, digits
from random import choices, randint
from re import fullmatch



class EmailValidator:
    ALLOWED_CHARSET = ascii_letters + digits + "_."
    MIN_LEN = 6
    MAX_LEN = 30
    DOMAIN = "gmail.com"
    EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    
    def __new__(cls): # objects now allowed
        return None
    
    @classmethod
    def get_random_email(cls):
        return f"{''.join(choices(cls.ALLOWED_CHARSET, k=randint(cls.MIN_LEN, cls.MAX_LEN)))}@{cls.DOMAIN}"
        
    @classmethod
    def check_email(cls, email:str):
        if not cls.__is_email_str:
            return False
        if email.find("..") > -1:
            return False
        return fullmatch(cls.EMAIL_REGEX, email) is not None        
            
    @staticmethod
    def __is_email_str(email):
        return True if type(email) == str else False


# em = EmailValidator() # None
# email = EmailValidator.get_random_email()
# EmailValidator.check_email(email)
# print(EmailValidator.check_email("sc_lib@list.ru")) # True
# print(EmailValidator.check_email("sc_lib@list_ru")) # False

assert EmailValidator.check_email("sc_lib@list.ru") == True
assert EmailValidator.check_email("sc_lib@list_ru") == False
assert EmailValidator.check_email("sc@lib@list_ru") == False
assert EmailValidator.check_email("sc.lib@list_ru") == False
assert EmailValidator.check_email("sclib@list.ru") == True
assert EmailValidator.check_email("sc.lib@listru") == False
assert EmailValidator.check_email("sc..lib@list.ru") == False # here
