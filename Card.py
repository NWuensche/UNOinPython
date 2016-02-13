import random
import os
from enum import Enum

CONST_START_NUMBER_OF_HANDS = 7


class Colors(Enum):
    blue = 0
    red = 1
    yellow = 2
    green = 3


class Values(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    draw2 = 11
    skip = 12
    revese = 13


class Card():

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color.name

    def getValue(self):
        return self.value.name


def createColorStack(color):
    colorStack = []

    if(color.value < 4):
        for value in Values:
            if(value.value == 0):
                colorStack.append(Card(color, value))
            else:
                colorStack.append(Card(color, value))
                colorStack.append(Card(color, value))
    return colorStack


def initStackOfCards():
    cardStack = []
    for color in Colors:
        cardStack.extend(createColorStack(color))
    return cardStack


def shuffleDeckofCards(stack):
    for i in range(1000):
        r1 = random.randrange(len(stack))
        r2 = random.randrange(len(stack))
        stack[r1], stack[r2] = stack[r2], stack[r1]


def drawCard(stack):
    return(stack.pop(0))


def initHand(stack):
    hand = []
    for card in range(CONST_START_NUMBER_OF_HANDS):
        hand.append(stack.pop(0))
    return hand


def someoneWon(handsOfCards):
    for hand in handsOfCards:
        if len(hand) == 0:
            return True
    return False


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


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def showCurrentScreen(hand, direction, lastCard):
    clearScreen()
    showDirection(direction)
    showLastCard(lastCard)
    showHand(hand)


def playCard(hand):
    try:
        whichCard = int(input("Which Card you want to play: "))
        thrownCard = hand.pop(whichCard)
        return thrownCard
    except:
        print("Invalid Input")
        playCard(hand)


def showLastCard(lastCard):
    try:
        print("Last Card: " + str(lastCard.getValue()) +
              " " + str(lastCard.getColor()))
    except:
        print("Last Card: - ")
