from random import randint

class RandomPassword:
    def __init__(self, charset, min_len, max_len):
        self.__charset = charset
        self.__min_len = min_len
        self.__max_len = max_len
        
    def __call__(self):
        charset_len = len(self.__charset)
        pass_len = randint(self.__min_len, self.__max_len)
        return ''.join(([self.__charset[randint(0, charset_len)-1] for _ in range(pass_len)]))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
    
rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)