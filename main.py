import Card
import CurrentScreen

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(
    cardStack), Card.initHand(cardStack), Card.initHand(cardStack)]
whichPlayer = 0
thrownCards = []
# direction 1: clockwise, -1: counter-clockwise
direction = 1
lastCard = Card.drawCard(cardStack, thrownCards)
thrownCards.append(lastCard)
names = Card.getNames(numberOfPlayers)
drawCards = 0
while Card.someoneWon(handsOfCards) == False:
    CurrentScreen.showCurrentScreen(
        handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer],drawCards)
    # objekte mit 5 objteken machen
    lastCard = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                            False, names[whichPlayer], direction, thrownCards,drawCards)
    if lastCard.getValue() == "draw2":
        drawCards += 2
    elif lastCard.getValue() == "reverse":
        direction *= -1
    elif lastCard.getValue() == "skip":
        whichPlayer = (whichPlayer + 1) % numberOfPlayers
    thrownCards.append(lastCard)
    whichPlayer = (whichPlayer + 1) % numberOfPlayers
