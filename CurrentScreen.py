import os


def showDirection(direction):
    if(direction == 1):
        print("Direction: Clockwise\t", end="")
    else:
        print("Direction Counter-Clockwise", end="")


def showHand(hand):
    whichCard = 0
    for card in hand:
        print("" + str(card.getValue()) + " " +
              str(card.getColor()) + " -> " + str(whichCard))
        whichCard += 1
    print()
    print("Pass -> P")
    print("Draw 1 Card -> D")


def showCurrentScreen(hand, direction, lastCard, playerName):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showLastCard(lastCard)
    showHand(hand)


def showPlayerName(playerName):
    print("Name: " + playerName + "\t", end="")


def showLastCard(lastCard):
    try:
        print("Last Card: " + str(lastCard.getValue()) +
              " " + str(lastCard.getColor()))
    except:
        print("Last Card: - ")


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")