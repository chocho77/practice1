my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(f'Number of iteration : {i}')
    print("Enter a string with this pathern: {number,number,number} Example: {1,2,3}")
    pathern = input()
    pathern = pathern.lstrip("{").rstrip("}")
    pathern = pathern.split(",")
    num1 = int(pathern[0])
    num2 = int(pathern[1])
    num3 = int(pathern[2])
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')
    print(f'num3 = {num3}')
    print(f'Sum = {num1+num2+num3}')



