from animals import Lion, Elephant
from battle import Battle

lion = Lion("Simba")
elephant = Elephant("Dumbo")

battle = Battle(lion, elephant) 

battle.start()
battle.result()