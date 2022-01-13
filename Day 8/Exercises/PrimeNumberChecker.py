# Write your code below this line 👇
import math

def prime_checker(number):

    isPrime = True
    for num in range(2,number):
        if number % num == 0:
            isPrime = False

    if not isPrime:
        print("Not a prime")
    else:
        print("Is Prime")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


