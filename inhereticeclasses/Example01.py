class Animal:
    def makeSound(self):
        print("Roar")

class Dog(Animal):    # inherites class Animal
    pass

class Cat(Animal):
    pass


sam = Dog()
Cat().makeSound()
sam.makeSound()

