import pet

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

Duke = pet.Pet("Duke", "dog", "play dead")
Maria = Ninja("Maria", "Arriviello", Duke, "Bones","Kibble")
Maria.walk().feed().bathe()