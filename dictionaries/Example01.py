my_dict = {
    "a" : "alpha",
    "o" : "omega",
    "g" : "gamma"
}

print(my_dict['a'])
print(my_dict['g'])
print(my_dict['o'])


for _ in range(3):
    print("----")
print("keys", "-", "values")
for n in my_dict:
    print(n, "  -  ", my_dict[n])

for _ in range(2):
    print("----")

print(hash(my_dict["a"]))

print("-----")
