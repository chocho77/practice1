import math
def polynom() -> None:
    print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
    lst = []
    for i in range(0, 4):
        a = int(input("Enter coefficient:"))
        lst.append(a)
    x = int(input("Enter the value of x :"))
    sum1 = 0
    j = 3
    for i in range(0, 3):
        while j > 0:
            sum1 = sum1 + (lst[i] + math.pow(x, j))
            break
        j = j - 1
    sum1 = sum1 + lst[3]
    print('The value of the polynomal is :', sum1)


if __name__ == '__main__':
    polynom()

