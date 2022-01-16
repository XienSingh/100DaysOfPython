import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

users_cards = []
computers_cards = []
gameIsRunning = input("Start New Game?").lower() == "y"
playersTotal = 0
computerTotal = 0


def deal_start_hand():
    computers_cards.extend(random.sample(cards, 2))
    users_cards.extend(random.sample(cards, 2))

def get_totals():
    global computerTotal
    global playersTotal
    computerTotal = 0
    playersTotal = 0

    for num in computers_cards:
        computerTotal += num
    for num in users_cards:
        playersTotal += num


def add_card(cardsItem, number):
        cardsItem.extend(random.sample(cards,number))
        print(cardsItem)


def play_dealer():
    get_totals()

    if (computerTotal == 21 and playersTotal == 21):
        print("Draw - Black Jack")
        gameIsRunning = False
    elif(computerTotal == 21):
        print("House Wins")
        gameIsRunning = False
    elif (computerTotal < 21 and playersTotal > computerTotal):
        add_card(computers_cards,1)
        play_dealer()
    elif computerTotal < 22 and computerTotal > playersTotal:
        print("House wins")
        gameIsRunning = False
    elif computerTotal > 21:
        print("House loses! You win!!!")
        gameIsRunning = False
        return


def play_user():
    global gameIsRunning
    decision = input("What would you like to do? Hit - new card, Stand - do nothing, end - exit")
    if decision.lower() == "hit":
        add_card(users_cards, 1)
    elif decision.lower() == "stand":
        play_dealer()
    elif decision.lower() == "end":
        gameIsRunning = False
        return
    get_totals()
    if playersTotal < 22:
        play_user()
    elif playersTotal > 21:
        gameIsRunning = False
        return


def StartGame():
    while gameIsRunning:
        deal_start_hand()
        print(users_cards)
        print(computers_cards)

        get_totals()

        if(playersTotal == 21):
            print("You Win - Black Jack")
        elif playersTotal < 21 and computerTotal < 22:
            play_user()
        elif playersTotal > 21:
            print("You lose")


StartGame()
