class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume 
        self.measure = measure
        
    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"
    
    def __repr__(self) -> str:
        return self.__str__()
        
class Recipe:
    def __init__(self, *args):
        self.ing_lst = list(args)
        
    def add_ingredient(self, ing):
        """добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);"""
        self.ing_lst.append(ing)
        
    def remove_ingredient(self, ing):
        """удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;"""
        self.ing_lst.remove(ing) 
        
    def get_ingredients(self):
        """получение кортежа из объектов класса Ingredient текущего рецепта."""
        return tuple(self.ing_lst)

    def __len__(self):
        """возвращает число ингредиентов в рецепте."""
        return len(self.ing_lst)
    
    def __str__(self):
        return ','.join([str(item) for item in self.ing_lst])


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
print(recipe)
ings = recipe.get_ingredients()
print(ings)
n = len(recipe) # n = 3
print(n)