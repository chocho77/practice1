if __name__ == '__main__':
    # Input validation
    user_input = input("Enter phone number:")
    if user_input.isdigit():
        phone_number = user_input
        print(phone_number)
    else:
        print("Wrong input.")