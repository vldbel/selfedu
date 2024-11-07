import time

class GeyserClassic:
    MAX_DATE_FILTER = 100
    
    def __init__(self):
        self.mechanical = None # для очистки от крупных механических частиц;
        self.aragon = None # для последующей очистки воды;
        self.calcium = None # для обработки воды на третьем этапе.
        
    def add_filter(self, slot_num, filter):
        if slot_num == 1 and not self.mechanical and isinstance(filter, Mechanical): 
            self.mechanical = filter
        elif slot_num == 2 and not self.aragon and isinstance(filter, Aragon):
            self.aragon = filter
        elif slot_num == 3 and not self.calcium and isinstance(filter, Calcium):
            self.calcium = filter
            
    def remove_filter(self, slot_num):
        """извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);"""
        if slot_num == 1: 
            self.mechanical = None
        elif slot_num == 2: 
            self.aragon = None
        elif slot_num == 3: 
            self.calcium = None
                    
    def get_filters(self):
        """возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);"""
        return (self.mechanical, self.aragon, self.calcium)

    def water_on(self):
        """включение воды: возвращает True, если вода течет и False - в противном случае."""
        if all((self.mechanical, self.aragon, self.calcium)) \
                and self.check_validity(self.mechanical) \
                and self.check_validity(self.aragon) \
                and self.check_validity(self.calcium):
            return True
        return False
    
    def check_validity(self, filter):
        # print("validator: ", type(filter), time.time() - filter.date)
        if time.time() - filter.date > self.MAX_DATE_FILTER:
            # print('out of date')
            return False 
        else:
            # print('ready to work')
            return True

class Mechanical:
    def __init__(self, instal_date):
        self.date = instal_date
    
    def __setattr__(self, name: str, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)


class Aragon:
    def __init__(self, instal_date):
        self.date = instal_date

    def __setattr__(self, name: str, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)
        
class Calcium:
    def __init__(self, instal_date):
        self.date = instal_date

    def __setattr__(self, name: str, value):
        if name == 'date' and name in self.__dict__:
            return
        super().__setattr__(name, value)
    

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
# print(w)
# my_water.add_filter(3, Calcium(time.time()))
# print(my_water.mechanical.date, my_water.aragon.date, my_water.calcium.date)
# w = my_water.water_on() # True
# print("Must be True:", w)
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# print(my_water.mechanical.date, my_water.aragon.date, my_water.calcium.date)
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
# print(my_water.mechanical.date, my_water.aragon.date, my_water.calcium.date)