class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
        
    def show(self):
        """для отображения окна на экране (выводит в консоль строку в формате: , например "Диалог 1: 100, 50")."""
        print(f"{self.__title}: {self.__width}, {self.__width}")

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not self.check_size(width):
            return
        if self.__width != width:
            self.__width = width
            self.show()
    
    @property
    def height(self):
        return self.__height
    
    @height.setter     
    def height(self, height):
        if not self.check_size(height):
            return
        if self.__height != height:
            self.__height = height
            self.show()
        
    def check_size(self, size):
        return True if type(size) == int and (0 <= size <= 10_000) else False

            
wnd = WindowDlg("заголовок окна", 400, 200)
