#!/usr/bin/python

class PhoneNumber:
    def  __init__(self, digits):
        self._digits = digits
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= len(self._digits):
            raise StopIteration
        digit = self._digits[self._current]
        self._current += 1 
        return digit

my_phone_number = PhoneNumber("085124124")
for digit in my_phone_number:
   print(digit)




