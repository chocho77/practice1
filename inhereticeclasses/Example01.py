class Animal:
    def makeSound(self):
        print("Roar")

class Dog(Animal):    # inherites class Animal
    pass

sam = Dog()
sam.makeSound()
