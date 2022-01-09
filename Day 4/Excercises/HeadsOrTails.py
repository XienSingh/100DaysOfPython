import random as rand

headOrTail = rand.randint(0,1)

if headOrTail == 1:
    print("Heads")
elif headOrTail == 0:
    print("Tails")
else:
    print("Error")