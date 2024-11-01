def heap_stack() -> None:
    a = 3
    b = 4
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    a = 5
    b = 5
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")


if __name__ == '__main__':
    heap_stack()




