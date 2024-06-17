#!/usr/bin/python

seq = ['foo', 'bar']
#  loop
for x in seq:
    print(x)

print("----")
# iterator

iterator = iter(seq)
while True:
    try:
        print(next(iterator))
    except StopIteration as e:
        break



