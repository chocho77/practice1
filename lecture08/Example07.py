def sol() -> None:
    l = [1, 2, 3]
    print("First variant to check list isn't empty.")
    if not l:
        print("List is empty.")
    else:
        print("List is not empty.")
    print("Second variant to check list isn't empty.")
    if l:
        print("List is not empty.")
    else:
        print("List is empty.")


if __name__ == '__main__':
    sol()

