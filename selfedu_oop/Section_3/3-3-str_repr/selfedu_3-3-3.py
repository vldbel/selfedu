class Model:
    def __init__(self):
        self.dct = {}
    
    def query(self, **kwargs):
        self.dct.update(kwargs)

    def __str__(self) -> str:
        if not self.dct:
            return "Model"
        formatted_out = ', '.join([str(k) + " = " + str(v) for k, v in self.dct.items()])
        return f"Model: {formatted_out}"
        # "Model: id = 1, fio = Sergey, old = 33"
        
    
model = Model()
model.query(id=1, fio='Sergey', old=33)
model.query(id=2, fio='Misha', old=44)
print(model)