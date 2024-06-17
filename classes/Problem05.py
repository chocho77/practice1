class Cat:

    def cat_desc():
        print("The cat is animal.")

    def __init__(self, name):
        self.name = name
        print(f"The cat {self.name} is created.")
    
    def meow(self):
        print(f"The cat {self.name} say meow.")


cat1 = Cat("Sparki")
cat2 = Cat("Erqul")

cat1.meow()
cat2.meow()

Cat.cat_desc()