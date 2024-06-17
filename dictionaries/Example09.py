dic1 = {
    0: "zero",
    1: "one",
    2: "two"
}

dic2 = {
    "Key-1": "Value-1",
    "Key-2": "Value-2"
}

main_dic = {}
main_dic[0] = dic1
main_dic[1] = dic1
main_dic[2] = dic2
main_dic[3] = dic2

print(main_dic)
print()

for key, val in main_dic.items():
    print(key, val)


print()
for i in range(3):
    print(main_dic[0][i])

print()


