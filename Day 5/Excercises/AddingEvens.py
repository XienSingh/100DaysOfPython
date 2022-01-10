# Calculate the sum of all even numbers from 1 to 100

evenSum = 0

for number in rangeF(1,101):
    if number % 2 == 0:
        evenSum += number

print(evenSum)