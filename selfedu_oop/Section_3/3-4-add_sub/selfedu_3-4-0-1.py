class Clock:
    __DAY = 60 * 60 * 24
    
    def __init__(self, seconds: int) -> None:
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be an integer")
        self.seconds = seconds
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    def __add__(self, second):
        
        if isinstance(second, self.__class__):
            second = second.seconds
        return Clock(self.seconds + second)
    
    def __str__(self) -> str:
        return self.get_time()
    
    @staticmethod
    def __get_formatted(x):
        return str(x).rjust(2, "0")
    

c1 = Clock(1000)
c1.seconds = c1.seconds + 100
c1 = c1 + 100   
print(c1.get_time())
c2 = Clock(2000)
c3 = c1 + c2
print(c3)



