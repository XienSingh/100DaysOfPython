import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# 0 - Rock
# 1 - Paper
# 2 - Scissors

humanChoice = int(input("Please press 0 for Rock, 1 for Paper or 2 for scissors"))

listOfChoices = [rock,paper,scissors]
print(f"Your choice: \n {listOfChoices[humanChoice]}")

computerChoice = random.randint(0, 2)
print(f"Computer choice: \n {listOfChoices[computerChoice]}")


if humanChoice >= 3 or humanChoice < 0:
    print("Invalid number, you lose!")
elif humanChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and humanChoice == 2:
    print("You lose")
elif computerChoice > humanChoice:
    print("You lose")
elif humanChoice > computerChoice:
    print("You win!")
elif computerChoice == humanChoice:
    print("It's a draw")
