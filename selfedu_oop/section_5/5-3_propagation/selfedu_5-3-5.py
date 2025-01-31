"""Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию."""

class Test:
    DESCR_MIN_LENGTH = 10
    DESCR_MAX_LENGTH = 10000

    def __init__(self, descr):
        self.descr = self._check_descr(descr)

    def _check_descr(self, descr):
        if not (self.DESCR_MIN_LENGTH < len(descr) <= self.DESCR_MAX_LENGTH):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        return descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = self._check_num(ans_digit)
        self.max_error_digit = self._check_positive(self._check_num(max_error_digit))

    @staticmethod
    def _check_num(val):
        if not type(val) in (int, float):
            raise ValueError('недопустимые значения аргументов теста')
        return val
    
    @staticmethod
    def _check_positive(val):
        if val < 0:
            raise ValueError('недопустимые значения аргументов теста')
        return val
    
    def run(self):
        ans = float(input()) # именно такой командой, ее прописывайте в методе run()
        return True if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit else False
    

# descr, ans = map(str.strip, input().split('|'))
# try:
#     testAnsDigit = TestAnsDigit(descr,float(ans))
#     print(testAnsDigit.run())
# except Exception as e:
#     print(e)


try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

    
try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False