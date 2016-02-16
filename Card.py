import random
import CurrentScreen
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


def drawCard(stack, thrownCards):
    try:
        return(stack.pop(0))
    except:
        stack = reshuffle(stack)
        return drawCard(stack, thrownCards)


def reshuffle(thrownCards):
    return shuffleDeckofCards(thrownCards)
    # todo hier weitermachen


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


def sameColor(card, lastCard):
    if card.getColor() == lastCard.getColor():
        return True
    return False


def sameValue(card, lastCard):
    if card.getValue() == lastCard.getValue():
        return True
    return False


def canBeThrown(card, lastCard):
    if(sameColor(card, lastCard) or sameValue(card, lastCard)):
        return True
    return False


def playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, thrownCards):
    whichCard = input("Which Card you want to play: ")
    # TODO better handling with ^c, ^d
    if whichCard == "d" or whichCard == "D":
        if hasDrawnCard == False:
            hand.append(drawCard(cardStack, thrownCards))  # Fehler?
            hasDrawnCard = True
            CurrentScreen.showCurrentScreen(hand, direction, lastCard, playerName)
        else:
            print("You already have drawn a card!")
        # TODO Stackoverflow how can i prevent 5 paramters and more
        return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, thrownCards)
    if whichCard == "p" or whichCard == "P":
        # pass Turn
        if(hasDrawnCard == True):
            return lastCard
        print("You first have to draw a card!")
        return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, thrownCards)
    try:
        print("Color"+hand[int(whichCard)].getColor()+ " Value" + hand[int(whichCard)].getValue())
        print("Color"+lastCard.getColor()+ " Value" + lastCard.getValue())
        if(canBeThrown(hand[int(whichCard)], lastCard)):
            thrownCard = hand.pop(int(whichCard))
            return thrownCard
        else:
            print("Can't be thrown!")
            return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, thrownCards)
    except:
        print("Error!")
        return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, thrownCards)


def getNames(numberOfPlayers):
    names = []
    for i in range(numberOfPlayers):
        names.append(input("What's the name of Player " + str(i + 1) + " "))
    return names

# TODO dont draw 2 card in one round
