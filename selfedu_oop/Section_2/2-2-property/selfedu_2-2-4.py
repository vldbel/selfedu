class Car:
    def __init(self, model):
        self.__model
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        if type(model) == str and (2 <= len(model) <= 200): 
            self.__model = model
        
        
car = Car()
car.model = "Toyota"    
print(car.model)
        