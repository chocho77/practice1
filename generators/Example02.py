#!/usr/bin/python

def even_numbers():
    for i in range(10):
        if i% 2 == 0:
            yield i


for even in even_numbers():
    print(even)

