# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

squareHeight = float(height) ** 2
mass = float(weight)
BMI = mass/squareHeight

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
bmiRating = ""
if BMI < 18.5:
    bmiRating = "Underweight"
elif BMI > 18.5 and BMI < 25:
    bmiRating = "Normal"
elif BMI > 25 and BMI < 30:
    bmiRating = "Slightly overwieght"
elif BMI > 30 and BMI < 35:
    bmiRating = "Obese"
elif BMI > 35:
    bmiRating = "Clinically obese"

print(f"A BMI of {int(BMI)} means you are {bmiRating}")
