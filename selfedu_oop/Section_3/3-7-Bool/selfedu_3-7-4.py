class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __len__(self):
        return self.score
    
    def __str__(self):
        return f"{self.name} ({self.old}): {self.score}"
    
    def __repr__(self):
        return self.__str__()
    

lst_in = ['Балакирев; 34; 2048',
            'Mediel; 27; 0',
            'Влад; 18; 9012',
            'Nina P; 33; 0']

players = [line.split("; ") for line in lst_in]
players = [Player(line[0], int(line[1]), int(line[2])) for line in players]

players_filtered = list(filter(bool, players))
print(players_filtered)