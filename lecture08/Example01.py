def solution() -> None:
    num_list = [1, "2.4", "3", ["Hello", 2, [1,2,3]], True] # Create a list
    print(num_list)
    num_list[3] = "Hello"
    print(num_list)
    num_list_copy = num_list.copy()
    print(num_list_copy)


if __name__ == '__main__':
    solution()


