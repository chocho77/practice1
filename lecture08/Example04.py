# removed elements from the list

def sol_one() -> None:
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    removed_element = my_list.pop(0)
    print(my_list)
    print(removed_element)
    removed_element = my_list.pop(1)
    print(my_list)
    print(removed_element)

def sol_two() -> None:
    #use remove method
    my_list = [1,2,3,4,5,5,5,5,5]
    print(my_list)
    while 5 in my_list:
        my_list.remove(5)
    print(my_list)


if __name__ == '__main__':
    sol_one()
    print("----")
    sol_two()

