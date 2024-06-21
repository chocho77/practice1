def fun()-> {}: # type: ignore
    d = {"key1": "val1",
         "key2": "val2"
         }
    return d

def fun1()-> []: # type: ignore 
    l = []
    l.append(1)
    l.append(2)
    l.append(3)

    return l

d1 = fun()
print(d1)
l = fun1()
print(l)
