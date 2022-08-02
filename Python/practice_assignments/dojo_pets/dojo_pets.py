class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    #walk ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    #feed ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self

    #clean ninja's pet invoking pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

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

Duke = Pet("Duke", "dog", "play dead")
Maria = Ninja("Maria", "Arriviello", Duke, "Bones","Kibble")
#print(Maria.pet.name)

# Duke.sleep()
# Duke.eat()
# print(Duke.energy)

Maria.walk().feed().bathe()


