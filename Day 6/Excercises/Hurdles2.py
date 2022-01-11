def doHurdles():
    move()
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()


def turnRight():
    turn_left()
    turn_left()
    turn_left()


keepGoing = True
while keepGoing:
    if (at_goal()):
        keepGoing = False
    else:
        doHurdles()

