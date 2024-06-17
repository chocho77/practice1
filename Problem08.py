pathern = input()
pathern = pathern.lstrip("{").rstrip("}").split(",")
num1 = float(pathern[0])
num2 = float(pathern[1])
print(pathern)
print(f'num1 + num2 = {num1 + num2}')

