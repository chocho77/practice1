class Animal:
    def __init__(self, name) -> None:
        self._name = name

    def makeSound(self):
        print("Roar")

class Dog(Animal):    # inherites class Animal
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    @property
    def name(self):
        return self._name


sam = Dog("Sam")
cat = Cat("Tom")
print(sam.name)
print(cat.name)

sam.makeSound()
cat.makeSound()

