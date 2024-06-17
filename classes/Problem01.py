#!/bin/python
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f'My name is {self.name}.')
        print(f'My color is {self.color}.')
        print(f'My weight is {self.weight} pounds.')

r1 = Robot("Robko", "red", "50")
r1.introduce_self()
r2 = Robot("Gradko", "green", "40")
r2.introduce_self()





