'''
    Battle Algorithm:
    1. Continue the battle while both animals have health above 0
    2. Randomly determine which animal attacks
    3. Calculate the damage inflicted by Animal 1's attack:
    3a: If the damage is positive: Update Animal 2's health by deducting the damage
    3b: Otherwise, Animal 2 successfully blocks the attack
    4: Display the updated health of both animals
    ''' 
    
import random
from termcolor import colored
import time
    
class Battle:
    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2
        
    def start(self):
        print("Battle has started!")
        
        while self.animal1.health > 0 and self.animal2.health > 0:
            
            if random.random() > 0.5:
                print(colored(f"{self.animal1.name} attacks {self.animal2.name}", "yellow"))
                
                damage = self.animal1.attack() - self.animal2.defense()
                
                if damage > 0:
                    self.animal2.update_health(damage)
                else:
                    print(colored(f"{self.animal2.name} defends the attack!", "red"))
            else:
                print(colored(f"{self.animal2.name} attacks {self.animal1.name}", "yellow"))
                
                damage = self.animal2.attack() - self.animal1.defense()
                
                if damage > 0:
                    self.animal1.update_health(damage)
                else:
                    print(colored(f"{self.animal1.name} defends the attack!", "red"))
                    
            print(f"Health of {self.animal1.name} is {self.animal1.health}")
            print(f"Health of {self.animal2.name} is {self.animal2.health}")
            print("-------------\n")
            time.sleep(1.5)
            
    def result(self):
        if self.animal1.health > 0:
            print(colored(f"{self.animal1.name} won!", "green"))
        elif self.animal2.health > 0:
            print(colored(f"{self.animal2.name} won!", "green"))