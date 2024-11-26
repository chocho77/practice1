def sol_one() -> None:
    fruits = ["apple","banana", "coconut", "orange"]
    print(fruits)
    remove_element = input("enter name of element to remove : ")
    try:
        fruits.remove(remove_element)
        print(fruits)
    except ValueError:
        print("The element is not found.")


if __name__ == '__main__':
    sol_one()