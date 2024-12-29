"""Подвиг 10 (на повторение). В программе объявлены два класса и глобальная переменная"""

CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == "windows":
            return cls.create_windows_filedialog(*args, **kwargs)
        elif CURRENT_OS == "linux":
            return cls.create_linux_filedialog(*args, **kwargs)

    def create_windows_filedialog(title, path, exts):
        """для создания объектов класса WindowsFileDialog;"""
        return WindowsFileDialog(title, path, exts)

    def create_linux_filedialog(title, path, exts):
        """для создания объектов класса LinuxFileDialog."""
        return LinuxFileDialog(title, path, exts)


dlg = FileDialogFactory("title", "path", "exts")
print(dlg, dlg.__dict__)