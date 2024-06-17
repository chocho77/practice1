class Person:

    def __init__(self, name):
        self._name = name

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


person = Person("Ivan")

print(person.name)

person.name = "New name"

print(person.name)
