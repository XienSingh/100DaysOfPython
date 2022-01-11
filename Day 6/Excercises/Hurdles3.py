def doHurdles():
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


while not at_goal():
    if wall_in_front():
        doHurdles()
    else:
        move()

