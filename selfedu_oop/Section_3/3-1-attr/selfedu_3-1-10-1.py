class GeyserClassic:
    MAX_DATE_FILTER = 100
    
    def __init__(self):
        self.mechanicalechanical = None # для очистки от крупных механических частиц;
        self.aragon = None # для последующей очистки воды;
        self.calcium = None # для обработки воды на третьем этапе.
        
    def add_filter(self, slot_num, filter):
        """добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3)"""
        match slot_num:
            case 1 if isinstance(filter, Mechanical): 
                self.mechanical = filter 
            case 2 if isinstance(filter, Aragon):
                 self.aragon = filter
            case 3 if isinstance(filter, Calcium):
                self.calcium = filter
            
    def remove_filter(self, slot_num):
        """извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);"""
        match slot_num:
            case 1: self.mechanical = None
            case 2: self.aragon = None
            case 3: self.calcium = None
                    
    def get_filters(self):
        """возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);"""
        return (self.mechanical, self.aragon, self.calcium)

    def water_on(self):
        """включение воды: возвращает True, если вода течет и False - в противном случае."""
        if all(self.mechanical, self.aragon, self.calcium) \
                and self.mechanical.date < self.MAX_DATE_FILTER \
                and self.aragon.date < self.MAX_DATE_FILTER \
                and self.calcium.date < self.MAX_DATE_FILTER:
            return True

class Mechanical:
    def __init__(self, instal_date):
        self.date
    
    def __setattr__(self, name: str, value):
        if name == 'date':
            return
    
class Aragon:
    def __init__(self, instal_date):
        self.date 

    def __setattr__(self, name: str, value):
        if name == 'date':
            return
        
class Calcium:
    def __init__(self, instal_date):
        self.date 

    def __setattr__(self, name: str, value):
        if name == 'date':
            return
    

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно