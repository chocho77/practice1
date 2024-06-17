#!/usr/bin/python

class Robot:
      def __init__(self):
          self.name=None    
      def print_name(self):
          print(f"My name is {self.name}")

robot = Robot()
robot.name = "Robko"
robot.print_name()
print(type(robot))

