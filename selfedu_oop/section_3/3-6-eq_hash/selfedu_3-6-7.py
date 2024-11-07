"""Подвиг 7. Объявите класс с именем DataBase """

class Record:
    rec_no = 1
    def __init__(self, fio:str, descr:str, old:int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.rec_no
        Record.rec_no += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __str__(self):
        return f"rec: {self.pk}, {self.fio}, {self.descr}, {self.old}"

    def __repr__(self):
        return self.__str__()


class DataBase:
    def __init__(self, path='userdatabase.csv'): 
        self.__path = path
        self.dict_db = {}

    def write(self, record):
        """для добавления новой записи в БД, представленной объектом record;"""
        if not self.dict_db.get(record):
            self.dict_db[record] = []
        self.dict_db[record].append(record)

    def read(self, pk):
        """Чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число);
        запись ищется в значениях словаря"""
        for records in self.dict_db.values():
            for record in records:
                if pk == record.pk:
                    return record

    def show(self):
        for key, value in self.dict_db.items():
            print(key, ": ", value)


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase()

for line in lst_in:
    data = line.split('; ') 
    db.write(Record(data[0], data[1], int(data[2])))

# print()
# print(db.read(1))
# print(db.read(5))
# print(db.read(2))

# d = tuple(db.dict_db.values())[0][0]
# assert type(d.descr) == str and type(d.fio) == str and type(d.old) == int, "значениями словаря должен быть список из объектов класса Rect с набором атрибутов: descr (строка), fio (строка), old (целое число)"

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"
db22345.write(r2)
r22 = db22345.read(7)

assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
    
if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"