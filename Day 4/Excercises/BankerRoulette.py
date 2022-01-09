# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random as rand

number_of_people = len(names)
random_Number = rand.randint(0 , number_of_people - 1)

who_is_going_to_pay = names[random_Number]
print(f"{who_is_going_to_pay} has to pay the bill")