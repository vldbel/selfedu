class InputDigits:
    def __init__(self, func):
        self.__fn = func
        
    def __call__(self):
        res:str = self.__fn()
        return list(map(int, res.split()))

input_dg = InputDigits(input)
res = input_dg()
print(res)

# "12 -5 10 83" -> [12, -5, 10, 83]     