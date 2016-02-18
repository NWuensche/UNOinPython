import Card
import CurrentScreen
import EnumsCards

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(
    cardStack), Card.initHand(cardStack), Card.initHand(cardStack)]
whichPlayer = 0
thrownCards = []
# direction 1: clockwise, -1: counter-clockwise
direction = 1
otherColor = -1
lastCard = Card.drawCard(cardStack)
names = Card.getNames(numberOfPlayers)
# drawCards[1] 0=> + Cards not drawn, 1=> are drawn
drawCards = [0, 0]
while Card.someoneWon(handsOfCards) == False:
    if(otherColor != -1):
        lastCard = Card.Card(EnumsCards.Colors(otherColor), lastCard.value)
        lastCard.backInDeck = 1
        otherColor = -1
    CurrentScreen.showCurrentScreen(
        handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    lastCardTmp = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                                False, names[whichPlayer], direction, drawCards)
    # objekte mit 5 objteken machen
    # listindex out of range bei 5 spielern?
    if(lastCard.backInDeck == 0):
        cardStack.append(lastCard)
        lastCard.backInDeck = 1
    Card.shuffleDeckofCards(cardStack)
    lastCard = lastCardTmp
    if lastCard.getValue() == "draw2":
        if lastCard.backInDeck ==  1:
            drawCards[0]=0
        else:
            drawCards[0] += 2
        #todo drawCards[1] weg
    elif lastCard.getValue() == "draw4" :
        if lastCard.backInDeck ==  1:
            drawCards[0]=0
        else:
            drawCards[0] += 2
        if(lastCard.getColor() == "wild"):
            otherColor = CurrentScreen.showChooseColorScreen("")
    elif lastCard.getValue() == "chooseColor" and lastCard.getColor() == "wild":
        otherColor = CurrentScreen.showChooseColorScreen("")
    elif lastCard.getValue() == "reverse":
        direction *= -1
        drawCards[1] = 0
    elif lastCard.getValue() == "skip":
        whichPlayer = (whichPlayer + 1*direction) % numberOfPlayers
        drawCards[1] = 0
    else:
        drawCards[1] = 0
    whichPlayer = (whichPlayer + 1 * direction) % numberOfPlayers

print("Congratulations to "+names[(whichPlayer-1*direction*-1)%numberOfPlayers]+" for winning the game!")

# TODO look, if first shown card is special card
# TODO Unterschiedlihce Namen pfilicht
