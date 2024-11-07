class Clock:
    def __init__(self, tm:int=0):
        self.__tm = tm
        
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__tm = tm
    
    def get_time(self):
        return self.__tm
    
    @classmethod
    def __check_time(self, tm):
        if type(tm) != type(int()):
            # raise ValueError("time value must be integer integer")
            return False
        if not (0 <= tm <= 100_000):
            # raise ValueError("Value must be in range of 0...100000")
            return False
        return True
        
clock = Clock()
clock.set_time(4530)
