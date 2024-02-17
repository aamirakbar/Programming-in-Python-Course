class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Dog(), Cat(), Dog(), Cat(), Cat()]

for animal in animals:
    animal.sound()