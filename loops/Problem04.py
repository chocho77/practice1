sum = 0
i = 0
while i < 5:
    user_input = input()
    if not user_input.isdigit():
        print("Not a numbeer")
        continue
    sum += int(user_input)
    i += 1
print(sum)

