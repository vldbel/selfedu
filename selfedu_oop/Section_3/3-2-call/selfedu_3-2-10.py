class InputValues:
    def __init__(self, render):
        self.render = render
        
    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return list(map(self.render, res.split()))
        return wrapper
        
class RenderDigit:       
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None

render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
