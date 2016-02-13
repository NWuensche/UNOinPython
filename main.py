import Card

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(cardStack)
                    ,Card.initHand(cardStack), Card.initHand(cardStack)]
whichPlayer = 0
#direction 1: clockwise, 0: counter-clockwise
direction = 1
lastCard = "no card"
while Card.someoneWon(handsOfCards) == False:
    Card.showCurrentScreen(handsOfCards[whichPlayer],direction,lastCard)
    lastCard = Card.playCard(handsOfCards[whichPlayer])
    whichPlayer = (whichPlayer + 1) % numberOfPlayers
