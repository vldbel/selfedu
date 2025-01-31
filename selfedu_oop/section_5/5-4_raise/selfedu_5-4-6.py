"""Подвиг 6. Объявите класс DateString для представления дат"""

class DateError(Exception):
    ...


class DateString:
    def __init__(self, date_string):
        self.date_string = self._validate_date(date_string)

    @staticmethod
    def _validate_date(date_string):
        try:
            dd, mm, yyyy = map(int, date_string.split('.'))
        except ValueError as e:
            raise DateError(str(e))
        
        if not (1 <= dd <= 32 and 1 <= mm <= 12 and 1 <= yyyy <= 3000):
            raise DateError('Неверный формат даты')
        return f"{dd:>02}.{mm:>02}.{yyyy:>04}"

    def __str__(self):
        return self.date_string
    

date_string = input()

try:
    date_obj = DateString(date_string)
except DateError as e:
    print(e)
else:
    print(date_obj)