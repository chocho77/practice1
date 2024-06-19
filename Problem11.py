a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("-------------------")
if a > b:
    if b > c:
        print(f'a = {a}')
if a > c:
    if c > b:
        print(f'a = {a}')
if b > a:
    if a > c:
        print(f'b = {b}')
if b > c:
    if c > a:
        print(f'b = {b}')
if c > a:
    if a > b:
        print(f'c = {c}')
if c > b:
    if b > a:
        print(f'c = {c}')




