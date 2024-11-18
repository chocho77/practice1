def solution() -> None:
    print("Solution : Test Message.")
    # using the try and except blocks , use tab to indent where necessary
    try:
        ans = float(input("Type a number to add:"))
        print("100 + {} = {}".format(ans, 100 + ans))
    except ValueError:
        print("You did not put valid number")



if __name__ == '__main__':
    solution()
