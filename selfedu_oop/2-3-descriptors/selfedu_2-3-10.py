class Telecast:
    def __init__(self, id: int, name: str, duration: int):
        self.__id = id  # порядковый номер (целое число)
        self.__name = name  # наименование телепередачи (строка)
        self.__duration = duration  # длительность телепередачи в секундах (целое число)

    @property
    def uid(self):
        "для записи и считывания из локального атрибута __id"
        return self.__id
    
    @uid.setter
    def uid(self, id):
        self.__id = id
    
    @property    
    def name(self):
        """для записи и считывания из локального атрибута __name"""
        return self.__name
    
    @name.setter    
    def name(self, name):
        """для записи и считывания из локального атрибута __name"""
        self.__name = name
    
    @property
    def duration(self):
        """для записи и считывания из локального атрибута __duration"""
        return self.__duration

    @duration.setter
    def duration(self, duration):
        """для записи и считывания из локального атрибута __duration"""
        self.__duration = duration
        
        
class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_telecast(self, tl):
        """добавление новой телепередачи в список items"""
        self.items.append(tl)
        
    def remove_telecast(self, indx):
        """удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее)"""
        for id, item in enumerate(self.items):
            if item.uid == indx:
                self.items.pop(id)
                break     


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
pr.remove_telecast(2)
