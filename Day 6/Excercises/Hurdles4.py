def doHurdles():
    turn_left()
    while wall_on_right():
        move()
    turnRight()
    move()
    turnRight()
    while front_is_clear():
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

