# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

maxAge = 90
ageDiff = maxAge - int(age)
daysTillDeath = ageDiff * 365
monthsTillDeath = ageDiff * 12
weeksTillDeath = ageDiff * 52

print(f"You have {daysTillDeath} days, {weeksTillDeath} weeks and {monthsTillDeath} months left.")
