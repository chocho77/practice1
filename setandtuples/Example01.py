#!/usr/bin/python

# declaring a set

s1 = set([1, 2, 3, 1])
s2 = {4, 4, 5}
print(type(s1), type(s2))
s1.add(5)        # using the add method to add new items to a set
s1.remove(1)     # using the remove method to get rid of the value 1
# notice when printed it removed the second "]" at the end
print(s1)
print(s2)


