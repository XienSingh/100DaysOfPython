# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


trueCount = 0
loveCount = 0

trueCount += name1.count("t")
trueCount += name1.count("r")
trueCount += name1.count("u")
trueCount += name1.count("e")

trueCount += name2.count("t")
trueCount += name2.count("r")
trueCount += name2.count("u")
trueCount += name2.count("e")

loveCount += name1.count("l")
loveCount += name1.count("o")
loveCount += name1.count("v")
loveCount += name1.count("e")

loveCount += name2.count("l")
loveCount += name2.count("o")
loveCount += name2.count("v")
loveCount += name2.count("e")

finalCount = int(str(trueCount) + str(loveCount))

if finalCount > 90 or finalCount < 10:
    print(f"Your score is {finalCount}. You go together like coke and mentos")
elif finalCount < 50 or finalCount > 50:
    print(f"Your score is {finalCount}. You are okay together")
else:
    print(f"Your score is{finalCount}.")
