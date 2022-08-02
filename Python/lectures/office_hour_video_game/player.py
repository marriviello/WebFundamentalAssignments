from email.base64mime import header_length
from turtle import speed
from unicodedata import name



class Player:
    all_players = []

    def __init__(self, data):
        self.name = data['name']
        self.health = 100
        self.strength = data['strength']
        self.speed = data['speed']
        self.weapons = []
        self.armor_rating = 0
        Player.all_players.append(self)
    
    def add_weapon(self,weapon):
        self.weapons.append(weapon)
        return self

    def use_weapon(self, enemy, weapon):
        print(f"{enemy.name} with {enemy.health} points of health is being attacked.")
        enemy.health -= weapon.damage
        if enemy.health > 0:
            print(f"His new health is {enemy.health}")
        else:
            print(f"{enemy.name} is dead!")

    @classmethod
    def print_all_player_names(cls):
        for this_player in cls.all_players:
            print(f"This player's name is {this_player.name}")


