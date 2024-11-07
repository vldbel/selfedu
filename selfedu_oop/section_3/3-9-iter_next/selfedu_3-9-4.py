class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration

    def __iter__(self):
        self.__value = self.start
        return self
    
    
g = GeomRange(1, 1.2, 2)


res = next(g); print(res); res = next(g)
print(res)


it = iter(g); res = next(g)
res = next(g)
for x in g: print(x)