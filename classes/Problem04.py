#!/usr/bin/python

if __name__ == '__main__':
    print("Test")

class Car:
    color = 'Red'


car = Car()

print(type(car))
print(car.color)

class Calc:
    # Static fields
    x = 5
    y = 6
    num_of_object = 0
    
    # Static methods
    def static_method():
        print("Static")

    # Constructor
    def __init__(self):
        Calc.num_of_object += 1

    def _sum(self):
        self.z = self.x + self.y
        return self.z
    def _sub(self):
        self.z = self.x - self.y
        return self.z

print(f'Number of object : {Calc.num_of_object}')
calc = Calc()
calc1 = Calc()
print(f'Number of object : {Calc.num_of_object}')
sum = calc._sum()
print(sum)
sub = calc._sub()
print(sub)
print()
print("--")
print()
Calc.static_method()




