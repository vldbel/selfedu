class Course:
    """класс, отвечающий за управление курсом в целом;"""
    def __init__(self, name:str):
        self.name = name
        self.modules = []

    def add_module(self, module):
        """добавление нового модуля в конце списка modules;"""
        self.modules.append(module)
        
    def remove_module(self, indx):
        """удаление модуля из списка modules по индексу в этом списке."""
        self.modules.pop(indx)
        
    # def __str__(self) -> str:
    #     return self.name
    
    
class Module: 
    """класс, описывающий один модуль (раздел) курса;"""
    def __init__(self, name):
        self.name = name
        self.lessons = []
    
    def add_lesson(self, lesson):
        """добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);"""
        self.lessons.append(lesson)
    
    def remove_lesson(self, indx):
        self.lessons.pop(indx)
        
    # def __str__(self) -> str:
    #     return self.name


    # def __repr__(self) -> str:
    #     return str(self.lessons)
    
            
class LessonItem:
    """класс одного занятия (урока)."""
    def __init__(self, title:str, practices:int, duration:int):
        self.title = title  # название урока (строка);
        self.practices = practices  # число практических занятий (целое положительное число);
        self.duration = duration  # общая длительность урока (целое положительное число).

    def __setattr__(self, name: str, value) -> None:
        if name in ("title") and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if name in ("practices", "duration") and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, name, value)

    def __getattr__(self, name: str):
        # При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
        return False
    
    def __delattr__(self, name: str) -> None:
        # Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
        if name in ("title", "practices", "duration"):
            return False
        super().__delattr__(self, name)
        
    # def __str__(self) -> str:
    #     return f"{self.title} :: {self.practices} : {self.duration}"

    # def __repr__(self) -> str:
    #     return f"{self.title} :: {self.practices} : {self.duration}"
    
        
course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)