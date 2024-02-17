import random

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        pass
    
    def defense(self):
        pass
    
    def update_health(self, damage):
        self.health -= damage
    
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, 50)
        
    def attack(self):
        return random.randint(5, 15)
    
    def defense(self):
        return random.randint(1, 5)
    
    
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, 70)
        
    def attack(self):
        return random.randint(3, 10)
    
    def defense(self):
        return random.randint(3, 8)