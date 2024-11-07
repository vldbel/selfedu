TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, name):
        if TYPE_OS == 1:
            obj = DialogWindows()
        else:
            obj = DialogLinux()
        obj.name = name
        return obj
      
    def __init__(self, name) -> None:
        self.name = name


# test
dlg = Dialog("name1")
print(dlg)

TYPE_OS = 2 # 1 - Windows; 2 - Linux
dlg = Dialog("name2")
print(dlg)
