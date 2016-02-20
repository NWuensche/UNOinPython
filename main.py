import Card
import CurrentScreen
import EnumsCards

#0: Player, 1: KI
numberOf = []
startPlayer = 0
numberOf.append(int(input("How many players? ")))
numberOf.append(int(input("How many computers? ")))
# direction 1: clockwise, -1: counter-clockwise
pointsOfPlayers = Card.initPointsOfPlayers(numberOf[0]+numberOf[1])
# drawCards[1] 0=> + Cards not drawn, 1=> are drawn
drawCards = [0, 0]
names = Card.getNames(numberOf[0])
names.extend(Card.getKINames(numberOf[1]))
# TODO show right person, that won one round
while(Card.someHasEnoughtPoints(pointsOfPlayers)==-1):
    cardStack = Card.initStackOfCards()
    Card.shuffleDeckofCards(cardStack)
    handsOfCards = []
    for player in range((numberOf[0]+numberOf[1])):
        handsOfCards.append(Card.initHand(cardStack))
    #TODO Wenn erste Karte + 2, dann zwar Farbe wechseln, aber nur +2
    direction = 1
    otherColor = -1
    lastCard = Card.drawCard(cardStack)
    whichPlayer = startPlayer
    startPlayer+=1
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
            drawCards[0] += 4
        if(lastCard.getColor() == "wild"):
            if "KI" in names[whichPlayer]:
                colorCardsInHand = [0,0,0,0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value<=4):
                        colorCardsInHand[card.color.value] += 1
                bestColor = colorCardsInHand.index(max(colorCardsInHand))
                otherColor = bestColor
            else:
                otherColor = CurrentScreen.showChooseColorScreen("",handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "chooseColor" and lastCard.getColor() == "wild":
        if "KI" in names[whichPlayer]:
            colorCardsInHand = [0,0,0,0]
            for card in handsOfCards[whichPlayer]:
                if(card.color.value<=4):
                    colorCardsInHand[card.color.value] += 1
            bestColor = colorCardsInHand.index(max(colorCardsInHand))
            otherColor = bestColor
        else:
            otherColor = CurrentScreen.showChooseColorScreen("",handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "reverse" and lastCard.backInDeck == 0:
        direction *= -1
        drawCards[1] = 0
    elif lastCard.getValue() == "skip" and lastCard.backInDeck == 0:
        whichPlayer = (whichPlayer + 1*direction) % (numberOf[0]+numberOf[1])
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
                drawCards[0] += 4
                if(lastCard.getColor() == "wild"):
                    if "KI" in names[whichPlayer]:
                        colorCardsInHand = [0,0,0,0]
                        for card in handsOfCards[whichPlayer]:
                            if(card.color.value<=4):
                                colorCardsInHand[card.color.value] += 1
                            bestColor = colorCardsInHand.index(max(colorCardsInHand))
                            otherColor = bestColor
                    else:
                        otherColor = CurrentScreen.showChooseColorScreen("",handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "chooseColor" and lastCard.getColor() == "wild":
            if "KI" in names[whichPlayer]:
                colorCardsInHand = [0,0,0,0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value<=4):
                        colorCardsInHand[card.color.value] += 1
                    bestColor = colorCardsInHand.index(max(colorCardsInHand))
                    otherColor = bestColor
            else:
                otherColor = CurrentScreen.showChooseColorScreen("",handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "reverse" and lastCard.backInDeck == 0:
            direction *= -1
            drawCards[1] = 0
        elif lastCard.getValue() == "skip" and lastCard.backInDeck == 0:
            whichPlayer = (whichPlayer + 1*direction) % (numberOf[0]+numberOf[1])
            drawCards[1] = 0
        else:
            drawCards[1] = 0
        whichPlayer = (whichPlayer + 1 * direction) % (numberOf[0]+numberOf[1])
    winningPerson =  (whichPlayer+1*direction*-1)%(numberOf[0]+numberOf[1])
    print("Congratulations to "+names[winningPerson]+" for winning this round!")
    Card.givePersonPoints(handsOfCards,winningPerson,pointsOfPlayers)
    CurrentScreen.showPointsOfPlayers(pointsOfPlayers,names)
    input("Press any key to continue")

print("Congratulations to "+names[(whichPlayer-1*direction*-1)%(numberOf[0]+numberOf[1])]+" for winning the game!")

# TODO look, if first shown card is special card
# TODO Unterschiedlihce Namen pfilicht
