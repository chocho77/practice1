class Cat:
    def __init__(self, 
                 name="",
                 age = 0):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
    

def print_cat():
    cat = Cat("Tom", 5)
    print(f'{cat.name} is a cat. {cat.name}\'s age is {cat.age} years.')

def print_message() -> str:
    return("Hello, user.")

def print_t():
    message = print_message()
    print(message)


if __name__ == '__main__':
    print_t()
    print_cat()





