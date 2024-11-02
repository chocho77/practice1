def exchange_values() -> None:
    x, y = 5, 10
    print(f"x = {x}, y = {y}")
    x, y = y, x
    print(f"x = {x}, y = {y}")


if __name__ == '__main__':
    exchange_values()