# Lecture 6 Loops
# To find these numbers which is divided to 7 and 5 in range(1500 and 2701 include)
#

for number in range(1500, 2701):
    if number % 5 == 0 and number % 7 == 0:
        print(number)

