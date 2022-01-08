# Conditionals

# if condition:
#    doThis()
# else:
#    doThisInstead()


####################################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Pay R100")
    elif age == 19:
        print("Sorry you pay R150")
    else:
      print("Pay R110")
else:
    print("You can not ride the rollercoaster.")


# Operators
# < - less than
# > - Greater Than
# >= - greather than and equal to
# <=  - less than and equal to
# == equal to
# != not equal to
