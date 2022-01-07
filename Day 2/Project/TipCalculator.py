print("Welcome to the tip calculator.")
billValue = input("What was the total bill? \n")
percentageTip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
totalPeople = input("How many people should pay?\n")

totalAfterTip = float(billValue) + (float(billValue) * (float(percentageTip) / 100))
totalSplit = totalAfterTip / float(totalPeople)
totalToPay = "{:.2f}".format(totalSplit)
print(f"Each Person is to pay: {totalToPay}")
