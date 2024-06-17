#!/usr/bin/python

class Calc:
    a:int
    b:int
    c:str    
    def print_sum(self, a ,b):
        self.a = a
        self.b = b
        print(f'{self.a+self.b}')


calc = Calc()
calc.a = 1
calc.b = 2
calc.c = "Add"
print(calc.c)
c = calc.a + calc.b
print(c)
calc.print_sum(5, 5)


