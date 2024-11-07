import sys

# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data
        
    def link(self, obj):
        self.next_obj = obj


# считывание списка из входного потока (эту строку не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

# здесь создаются объекты классов и вызываются нужные методы
head_obj = None
for item in lst_in:
    current_node = ListObject(item)
    if not head_obj:  # first node
        head_obj = current_node
        prev_node = current_node
        continue
    prev_node.next_obj = current_node
    prev_node = current_node

print(head_obj.next_obj.data)