
two_digit_number = input("Type a two digit number: ")

if len(two_digit_number) < 2:
        two_digit_number = input("Type a two digit number: ")

if len(two_digit_number) > 1:
    print(int(two_digit_number[0])+int(two_digit_number[1]))


