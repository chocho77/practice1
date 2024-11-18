# Python - List Comprehension Example

def solution_one() -> None:
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    new_list = []

    for x in fruits:
        if "a" in x:
            new_list.append(x)

    print(new_list)

    pass

def solution_two() -> None:
    # List Comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    new_list = [x for x in fruits if "a" in x]
    print(new_list)


if __name__ == '__main__':
    print("Solution one: ")
    solution_one()
    print("Solution two: ")
    solution_two()
