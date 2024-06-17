numbers = input()
numbers = numbers.split(",")
sum = 0
count = 0;
for num in numbers:
    count +=1
    
if count == 5:
    for num in numbers:
        num = int(num)    
        if 10 <= num <= 5555:
            sum += num
        else:
            print("Error: Out of range!")
            break; 
    print(f'sum = {sum}')
else:
    print("Wrong input!")

print("END")







