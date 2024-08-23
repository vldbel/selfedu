class AppStore:
    def __init__(self) -> None:
        self.app_list = []
    
    def add_application(self, app):
        """ добавление нового приложения app в магазин;"""
        if app in self.app_list:
            raise ValueError("app is already in the list")
        self.app_list.append(app)
    
    def remove_application(self, app):
        """ удаление приложения app из магазина;"""
        if app not in self.app_list:
            raise ValueError("App is not in the list")
        self.app_list.remove(app)
        
    def block_application(self, app):
        """ блокировка приложения app. 
            устанавливает локальное свойство blocked объекта app в значение True);"""
        if app not in self.app_list:
            raise ValueError("App is not in the list")
        for app_from_list in self.app_list:
            if app_from_list == app:
                app_from_list.blocked = True
                   
    def total_apps(self):
        """ возвращает общее число приложений в магазине."""
        return len(self.app_list)
    
        
class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
        
        
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)