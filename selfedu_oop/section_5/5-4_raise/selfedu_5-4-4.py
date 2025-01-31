"""Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception."""

class StringException(Exception):
    """descr"""


class NegativeLengthString(StringException):
    ...


class ExceedLengthString(StringException):
    ...


try:
    # здесь команда для генерации исключения
    raise ExceedLengthString()
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
