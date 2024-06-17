#!/usr/bin/python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
iterator = iter(l)

#print(next(iterator))
#print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
       break

print(dir(l))


