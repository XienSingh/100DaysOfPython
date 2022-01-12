import random as rand
import Art
import Words
# Step 1

import os

clearConsole = lambda: os.system('cls')


chosen_word = rand.choice(Words.word_list)

lives = 6
isAlive = 1
hasWord = False

word_placeholder = []
lenghtOfWord = len(chosen_word)
successfulLetters = 0

for letter in chosen_word:
    word_placeholder.append("_")

print(Art.logo)
print(f"Welcome to Hangman")

while not hasWord:
    print(Art.stages[lives])
    print(" ".join(word_placeholder))

    if lives == 0:
        hasWord = True
        print("You killed bob!")
        print(f"The word was: {chosen_word}")
        break

    guess = input("Please guess a letter. \n").lower()
    clearConsole()
    indexOfLetter = 0

    for letter in chosen_word:
        if guess == letter:
            word_placeholder[indexOfLetter] = guess
            successfulLetters += 1
            if lenghtOfWord == successfulLetters:
                print("You win!")
                hasWord = True
        elif guess not in chosen_word:
            lives -= 1
            break
        indexOfLetter += 1
    print(" ".join(word_placeholder))
