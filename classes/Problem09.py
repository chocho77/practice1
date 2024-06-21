# Parent class
class Person:
  def __init__(self, fname, lname):
    self._firstname = fname
    self._lastname = lname

  def printname(self):
    print(self._firstname, self._lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Child class
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
