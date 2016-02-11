import random
from enum import Enum


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
        return self.value


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
    for i in range(500):
        r1 = random.randrange(len(stack))
        r2 = random.randrange(len(stack))
        stack[r1],stack[r2] = stack[r2],stack[r1]
