def solution(num:int,check_num:int) -> None:
    _x = num
    print(f"num = {num}")
    print(f"check value = {check_num}")
    _check_num = check_num
    if _x > _check_num:
        print("X is greater than check value.")
    else:
        print("X is not greater than check value.")


if __name__ == '__main__':
    solution(5, 4)
    solution(6,7)
    solution(4,4)

    for i in range(10):
        for j in range(3):
            solution(i, j)






