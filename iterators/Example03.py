#!/usr/bin/python

name = "chavdar"

#print(dir(name))

iterator = iter(name)

while True:
    try:
        print(next(iterator), end=" ")
    except StopIteration:
        break

print("\n-----------------\n")
print(dir(name.__iter__()))

