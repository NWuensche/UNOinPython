import os


def showToDrawnCards(drawCards):
    print("+Cards: " + str(drawCards[0]) + "\t", end="")


def showDirection(direction):
    if(direction == 1):
        print("Direction: Clockwise\t", end="")
    else:
        print("Direction Counter-Clockwise\t", end="")


def showHand(hand):
    whichCard = 0
    for card in hand:
        print("" + str(card.getValue()) + " " +
              str(card.getColor()) + " \t->\t " + str(whichCard))
        whichCard += 1
    print()
    print("Pass -> P")
    print("Draw 1 Card -> D")


def showCurrentScreen(hand, direction, lastCard, playerName, drawCards):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showToDrawnCards(drawCards)
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

def showChooseColorScreen(startMessage):
    clearScreen()
    showChooseColorScreen(startMessage)
    print("Choose a new color:")
    print("blue\t->\tb")
    print("red\t->\tr")
    print("yellow\t->\ty")
    print("green\t->\tg")
    newColor = lower(input())
    if(newColor == "b" or newColor == "r" or newColor == "y" or newColor == "g"):
        return newColor()
    else:
        return startMessage("Not a color!")
