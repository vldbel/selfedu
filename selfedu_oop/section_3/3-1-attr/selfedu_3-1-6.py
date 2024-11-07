class Museum:
    def __init__(self, name):
        self.name = name  # название музея (строка);
        self.exhibits = []  # список экспонатов (изначально пустой список).

    def add_exhibit(self, obj):
        """добавление нового экспоната в музей (в конец списка exhibits);"""
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        """удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)"""
        self.exhibits.remove(obj)
    
    def get_info_exhibit(self, indx):
        """получение информации об экспонате (строка) по индексу списка (нумерация с нуля)."""
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"


class Picture:
    # локальные атрибуты: name - название; author - художник; descr - описание
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
    def __init__(self, name, location, descr):
        self.name = name
        self.author = location
        self.descr = descr

   
class Papyri:
    # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
    def __init__(self, name, date, descr):
        self.name = name
        self.author = date
        self.descr = descr


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)