def value_one_str() -> str:
    return "Name One"

def value_two_str() -> str:
    return "Name Two"

def exchange_values() -> None:
    val1, val2 = value_one_str(), value_two_str()
    print(f"val1 : {val1}, val2 : {val2}")
    val1, val2 = val2, val1
    print(f"val1 : {val1}, val2 :  {val2}")


if __name__ == '__main__':
    exchange_values()


