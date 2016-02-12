import random
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
        return self.color.value

    def getValue(self):
        return self.value.value


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
        print("Direction: Clockwise")
    else:
        print("Direction Counter-Clockwise")

def showHand(hand):
    whichCard = 0
    for card in hand:
        print(card.getValue() +" "+ card.getColor() + " -> " + whichCard )

def showCurrentScreen(hand,direction):
    showDirection(direction)
    showHand(hand)

def playCard(hand):
    whichCard = int(raw_input("Which Card you want to play"))
    return Card.pop(whichCard)
