# add elements in a list

def solution_one() -> None:
    # first variant use method append
    list_temp = [1, 2, 3, 4, 5]
    print(list_temp)
    list_temp.append(3)
    print(list_temp)
    for x in range(1, 9, 2):
        list_temp.append(x)

    print(list_temp)


def solution_two() -> None:
    # second variant use method insert(index, item)
    list_temp = [1,2,"Hello",True,"string"]
    print(list_temp)
    list_temp.insert(0,"New item")
    print(list_temp)


if __name__ == '__main__':
    print("Add elements in a list.")
    print("Solution one")
    solution_one()
    print("Solution two")
    solution_two()
    

