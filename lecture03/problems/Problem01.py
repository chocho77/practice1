def solution() -> None:
    name = "Misha"
    num = 6
    real_num = 5.67
    print("String: " + name)
    print("Integer: " + str(num))
    print("Real number: " + str(real_num))

    # still works for python 2 and 3
    name = "John"
    print("Hello, %s." % name) # Hello, John.

    # multiple variables formating
    # using printf
    first_name = "John"
    last_name = "Smith"
    print("Hello, %s %s" % (first_name, last_name))

    # print int variables
    # using printf
    print("%d %d" % (4, 5))

    #print float variables
    #using printf
    print("%.2f %.1f" % (4.5, 6.7))

    # Scientific notation
    #using printf
    print("%e" % 4.884563E05)


if __name__ == '__main__':
    solution()

