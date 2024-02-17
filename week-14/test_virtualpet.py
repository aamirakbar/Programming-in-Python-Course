import unittest
from virtualpet import VirtualPet

class TestVirtualPet(unittest.TestCase):
    
    def setUp(self):
        self.pet = VirtualPet("Fido", "Dog")

    def test_initial_values(self):
        self.assertEqual(self.pet.name, "Fido")
        self.assertEqual(self.pet.species, "Dog")
        self.assertEqual(self.pet.hunger, 50)
        self.assertEqual(self.pet.energy, 50)

    def test_feed(self):
        self.pet.feed()
        self.assertEqual(self.pet.hunger, 40)

    def test_play(self):
        self.pet.play()
        self.assertEqual(self.pet.energy, 30)
        self.pet.energy = 5  # Simulate low energy
        self.pet.play()
        self.assertEqual(self.pet.energy, 0)  # Check if energy doesn't go below 0


#unittest.main()