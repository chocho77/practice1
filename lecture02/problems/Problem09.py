def exchange_values(num1: int, num2: int) -> None:
    x, y = num1, num2
    print(f"x = {x}, y = {y}")
    x, y = y, x
    print(f"x = {x}, y = {y}")


if __name__ == '__main__':
    exchange_values(5,6)
    exchange_values(6,7)
    exchange_values(56,78)
