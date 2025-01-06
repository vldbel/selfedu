"""Подвиг 6 (про модуль abc)."""

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        ...
    
    @classmethod
    def get_id(cls):
        cls._id += 1
        return cls._id

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = -1

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.get_id()

    def get_pk(self):
        return self._id


form1 = ModelForm("Логин", "Пароль")
print(form1.get_pk())

form2 = ModelForm("Логин", "Пароль")
print(form2.get_pk())

form3 = ModelForm("Логин", "Пароль")
print(form3.get_pk())