from typing import List


def enter_numbers() -> List:
    _my_list = []
    for i in range(5):
        float_num = float(input("Enter a float number "))
        _my_list.append(float_num)
    return _my_list


def solution() -> None:
    _my_list = []
    _my_list = enter_numbers()
    _check_float_num = float(input("Enter check float number : "))
    for i in range(5):
        if _my_list[i] > _check_float_num:
            print(f"Float number {_my_list[i]} is greater than check float number {_check_float_num}.")
        else:
            print(f"Float number {_my_list[i]} is not greater than check float number {_check_float_num}.")


if __name__ == '__main__':
    solution()