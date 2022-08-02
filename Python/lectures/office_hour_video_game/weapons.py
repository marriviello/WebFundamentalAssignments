class Weapon:
    
    def __init__ (self,data):
        self.name = data['name']
        self.damage = data['damage']
        self.weight = data['weight']
        self.type = data['type']
