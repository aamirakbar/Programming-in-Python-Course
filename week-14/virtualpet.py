class VirtualPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.energy -= 20
        if self.energy < 0:
            self.energy = 0
