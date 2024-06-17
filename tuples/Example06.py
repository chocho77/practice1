#!/usr/bin/python

myTuple = (0, 1, 2, 3, 4)  # this is a tuple
myTupleNames = ("Chavdar", "Momchilov", "Ventsislav", "Florin", "Petkan")
myList = [] # this is a empty list

for i in myTuple:
    myList.append(i)

print(myList)
print(type(myList))
print(type(myTuple))
print((type(myTupleNames)))

d = {}  # empty dictionary

for i in myTuple:
    d[i] = myTupleNames[i]

print(d)
print()
print(type(d))

for key,val in d.items():
    print(key, val)
print()

print(myTupleNames[2:4])
print(myTupleNames[1:3])
mySliceTuple = myTupleNames[2:4]
print(mySliceTuple)


# d[1] = myTupleNames[0]
# d[2] = myTupleNames[1]
# d[3] = myTupleNames[2]
# d[4] = myTupleNames[3]
# d[5] = myTupleNames[4]

# print(d)

