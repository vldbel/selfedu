class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        """добавление нового приложения на смартфон (в конец списка apps);"""
        # print(self.apps, app, type(app), )
        if not len(tuple(filter(lambda x: type(x) == type(app), self.apps))):
            self.apps.append(app)
            
    def remove_app(self, app):
        """удаление приложения по ссылке на объект app."""
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"
    
    
class AppYouTube:
    """name = "YouTube", memory_max = 1024"""
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = 1024
        

class AppPhone:
    # name = "Phone", phone_list = словарь с контактами
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list



sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)