class Cat:
    
    def __init__(self, name):
        self.name = name

cat1 = Cat("Sparki")
cat2 = Cat("Erqul")

print(cat1.name)
print(cat2.name)

print(hash(cat1))
print(hash(cat2))


