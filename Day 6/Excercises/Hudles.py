def doHurdles(hurdlesToJump):
    for hudles in range(0, hurdlesToJump + 1):
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


doHurdles(5)

