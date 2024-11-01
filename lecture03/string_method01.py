def print_data() -> None:
    name = "matt"
    correct = name.capitalize()
    print(f"{name}")
    print(f"{correct}")
    print(f"id(name) = {id(name)}")
    print(f"id(correct) = {id(correct)}")


if __name__ == '__main__':
    print_data()
