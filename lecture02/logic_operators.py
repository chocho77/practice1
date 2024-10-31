x = int(input("Enter x = "))
y = int(input("Enter y = "))
my_list = []

if x == y:
    print("one")
    my_list.append("one")
    print("x == y")
if x != y:
    print("two")
    my_list.append("two")
    print("x!=y")
if x > y:
    print("three")
    my_list.append("three")
    print("x>y")
if x < y:
    print("four")
    my_list.append("four")
    print("x<y")
if x <= y:
    print("five")
    my_list.append("five")
    print("x<=y")
if x >= y:
    print("six")
    my_list.append("six")
    print("x>=y")

if x == y:
    print("seven")
    my_list.append("seven")
    print("x==y")
else:
    print("eight")
    my_list.append("eight")
    print("x!=y")

if x == y:
    print("nine")
    my_list.append("nine")
    print("x==y")
elif x != y:
    print("ten")
    my_list.append("ten")
    print("x!=y")
elif x > y:
    print("eleven")
    my_list.append("eleven")
    print("x>y")
elif x < y:
    print("twelve")
    my_list.append("twelve")
    print("x<y")
elif x <= y:
    print("thirteen")
    my_list.append("thirteen")
    print("x<=y")
elif x >= y:
    print("fourteen")
    my_list.append("fourteen")
    print("x>=y")

print(f"my_list : {my_list}")



