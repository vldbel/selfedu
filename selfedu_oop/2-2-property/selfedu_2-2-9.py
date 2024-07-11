class PathLines:
    START_X = 0
    START_Y = 0

    def __init__(self, *lines):
        self.__lines = []
        self.__lines.extend(lines)
            
    def add_line(self, line):
        self.__lines.append(line)

    def get_path(self):
        return self.__lines
    
    def get_length(self):
        """возвращает суммарную длину пути (сумма длин всех линейных сегментов);"""
        path_length = 0
        x0 = self.START_X
        y0 = self.START_Y
        for line in self.__lines:
            x1 = line.x
            y1 = line.y
            path_length += ((x1-x0)**2 + (y1-y0)**2)**0.5
            x0 = x1
            y0 = y1
        return path_length

    def __str__(self):
        return str(self.get_length())
    
class LineTo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    
    
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(p)