import Card
import CurrentScreen
import EnumsCards

numberOfPlayers = int(input("How many players? "))
# direction 1: clockwise, -1: counter-clockwise
pointsOfPlayers = Card.initPointsOfPlayers(numberOfPlayers)
# drawCards[1] 0=> + Cards not drawn, 1=> are drawn
drawCards = [0, 0]
names = Card.getNames(numberOfPlayers)
# TODO show right person, that won one round
while(Card.someHasEnoughtPoints(pointsOfPlayers)==-1):
    cardStack = Card.initStackOfCards()
    Card.shuffleDeckofCards(cardStack)
    handsOfCards = [Card.initHand(cardStack), Card.initHand(
        cardStack), Card.initHand(cardStack), Card.initHand(cardStack)]
    direction = 1
    otherColor = -1
    lastCard = Card.drawCard(cardStack)
    whichPlayer = 0
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
    while Card.someoneWon(handsOfCards) == False:
        if(otherColor != -1):
            lastCard = Card.Card(EnumsCards.Colors(otherColor), lastCard.value)
            lastCard.backInDeck = 1
            otherColor = -1
        CurrentScreen.showCurrentScreen(
            handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        lastCardTmp = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                                    False, names[whichPlayer], direction, drawCards,False)
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
    winningPerson =  (whichPlayer+1*direction*-1)%numberOfPlayers
    print("Congratulations to "+names[winningPerson]+" for winning this round!")
    Card.givePersonPoints(handsOfCards,winningPerson,pointsOfPlayers)
    CurrentScreen.showPointsOfPlayers(pointsOfPlayers,names)
    input("Press any key to continue")

print("Congratulations to "+names[(whichPlayer-1*direction*-1)%numberOfPlayers]+" for winning the game!")

# TODO look, if first shown card is special card
# TODO Unterschiedlihce Namen pfilicht
