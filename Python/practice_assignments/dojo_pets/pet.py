class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    #increase pet energy by 25
    def sleep(self):
        self.energy += 25
        print(f"After sleeping, {Maria.pet.name}'s energy is {Duke.energy}.")
    
    #increase pet energy by 5 and health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"After eating, {Maria.pet.name}'s energy is {Duke.energy} and his health is {Duke.health}.")

    #increase pet health by 5
    def play(self):
        self.health += 5
        print(f"After playing, {Maria.pet.name}'s health is {Duke.health}.")

    #print out noise
    def noise(self):
        print("Woof!")