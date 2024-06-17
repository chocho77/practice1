my_dic = {
    "key-1" : "Val-1",
    "key-2" : "Val-2",
    "key-3" : "Val-3",
    "key-4" : "Val-4",
    "key-5" : "Val-5",
}

print()

for key, val in my_dic.items():
    print(key, val)

print()

#check = {"key-1" : "Val-1"}
check ={}
check['key-1'] = "Val-1"
check['key-2'] = "Val-2"

for key, val in check.items():
    print(key, val)

print()
if "key-1" in my_dic.keys():
    print("Found.")
else:
    print("Not Found.")
if "key-2" in my_dic.keys():
    print("Found.")
else:
    print("Not Found.")

print()

# Find common keys in two Dictionary

a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}

for key in a:
	if key in b:
		print(key, end=" ")

print()
