"""Подвиг 9 (релакс). """

class Body:
    def __init__(self, name, ro, volume):
        """ name - название тела (строка); 
            ro - плотность тела (число: вещественное или целочисленное); 
            volume - объем тела  (число: вещественное или целочисленное)."""
        self.name = name
        self.ro = ro
        self.volume = volume
        self.mass = ro * volume
    
    def __str__(self):
        return f"name: {self.name}, mass: {self.mass}"
    
    def __eq__(self, other):
        return self.mass == other.mass if isinstance(other, Body) else other 
    
    def __gt__(self, other):
        return self.mass > other.mass if isinstance(other, Body) else other 
    
    def __ge__(self, other):
        return self.mass >= other.mass if isinstance(other, Body) else other

    def __lt__(self, other):
        return self.mass < other.mass if isinstance(other, Body) else other
    
    def __le__(self, other):
        return self.mass <= other.mass if isinstance(other, Body) else other

body1 = Body("Zver", 1.2, 100)
body2 = Body("Vova", 1, 120)
print(body1, body2)

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5