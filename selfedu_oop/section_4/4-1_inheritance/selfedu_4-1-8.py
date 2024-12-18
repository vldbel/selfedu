"""Подвиг 8. Вам необходимо создать множество классов для валидации (проверки) корректности данных."""

class Validator:
    def _is_valid(self, data):
        return True
    
    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and (self._min_value <= data <= self._max_value)


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and (self._min_value <= data <= self._max_value)
    

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
print(float_validator(0.9))

# # Test type validation
# for obj in [integer_validator, float_validator]:
#     counter = 0
#     for datatype_ in [10, 0.9, '0', True, None, [], tuple(), set(), dict()]:
#         try:
#             res = obj(datatype_)
#             counter += 1
#         except Exception as e:
#             print(e, datatype_)
#     assert counter == 1, 'Возможно валидатор отрабатывает не корректно'

# # Test out of range
# flag = False
# try:
#     test1 = integer_validator(10)
#     flag = True
# except Exception:
#     flag = False
# finally:
#     assert flag, 'Возможно не корректно отрабатывают граничные значения [от;до]'
#     flag = False

# try:
#     test2 = float_validator(1.0)
#     flag = True
# except Exception:
#     flag = False
# finally:
#     assert flag, 'Возможно не корректно отрабатывают граничные значения [от;до]'

# try:
#     test1 = integer_validator(11)
# except Exception:
#     flag = True
# finally:
#     assert flag, 'Возможно не сраьбатывает валидация за граничными значениями [от;до]'

# try:
#     test2 = float_validator(1.1)
# except Exception:
#     flag = True
# finally:
#     assert flag, 'Возможно не сраьбатывает валидация за граничными значениями [от;до]'