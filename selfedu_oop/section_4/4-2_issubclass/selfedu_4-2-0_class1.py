class SmartPhone:
    pass


class IPhone(SmartPhone):
    pass


phone = IPhone()


print(issubclass(SmartPhone, IPhone)) # вернет False, так как SmartPhone является базовым классом для класса IPhone
print('False') # print(issubclass(phone, SmartPhone)) # вернет True, так как объект phone связан с базовым классом SmartPhone
print(issubclass(IPhone, object)) # вернет True, так как все классы в Python 3.x неявно наследуются от класса object
print(issubclass(IPhone, SmartPhone)) # вернет True, так как IPhone является подклассом класса SmartPhone
print(issubclass(SmartPhone, IPhone)) # вернет True, так как SmartPhone связан с дочерним классом IPhone
print(isinstance(phone, SmartPhone)) # вернет True, так как объект phone связан с базовым классом SmartPhone