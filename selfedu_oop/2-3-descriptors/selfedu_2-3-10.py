class Thing:
    

class Bag:
    def __init__(self, max_weight):
        self.__things = []
        self.things = Things
    
    def add_thing(self, thing):
        """добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) 
            не будет превышен, иначе добавление не происходит)"""
            
    def remove_thing(self, indx):
        """удаление предмета по индексу списка __things;"""
        
    def get_total_weight(self):
        """возвращает суммарный вес предметов в рюкзаке."""
    
    
    
bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")