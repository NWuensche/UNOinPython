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
otherColor = "n"
lastCard = Card.drawCard(cardStack)
names = Card.getNames(numberOfPlayers)
#drawCards[1] 0=> + Cards not drawn, 1=> are drawn
drawCards = [0,0]
while Card.someoneWon(handsOfCards) == False:
    if(otherColor!="n"):
        CurrentScreen.showCurrentScreen(
            handsOfCards[whichPlayer], direction, Card(), names[whichPlayer], drawCards)
    CurrentScreen.showCurrentScreen(
        handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    # objekte mit 5 objteken machen
    lastCardTmp = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                                False, names[whichPlayer], direction, drawCards)
    #nicht karte, sondern farbe und wert übergeben
    if(lastCard.backInDeck == 0):
        cardStack.append(lastCard)
        lastCard.backInDeck = 1
    Card.shuffleDeckofCards(cardStack)
    lastCard = lastCardTmp
    # TODO 20 mal gleiche Karte auf Stack, wenn nur pass?
    if lastCard.getValue() == "draw2":
        drawCards[0] += 2
        if(drawCards[1] == 1):
            drawCards[0] = 0
    elif lastCard.getValue() == "draw4":
        drawCards[0] += 4
        if(drawCards[1] == 1):
            drawCards[0] = 0
        CurrentScreen.showChooseColorScreen()

    elif lastCard.getValue() == "reverse":
        direction *= -1
        drawCards[1] = 0
    elif lastCard.getValue() == "skip":
        whichPlayer = (whichPlayer + 1) % numberOfPlayers
        drawCards[1] = 0
    else:
        drawCards[1] = 0
    thrownCards.append(lastCard)
    whichPlayer = (whichPlayer + 1 * direction) % numberOfPlayers

# TODO look, if first shown card is special card
# TODO Unterschiedlihce Namen pfilicht
