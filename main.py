import Card
import CurrentScreen

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(
    cardStack), Card.initHand(cardStack), Card.initHand(cardStack)]
whichPlayer = 0
# direction 1: clockwise, 0: counter-clockwise
direction = 1
lastCard = Card.drawCard(cardStack)
names = Card.getNames(numberOfPlayers)
while Card.someoneWon(handsOfCards) == False:
    CurrentScreen.showCurrentScreen(
        handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer])
    lastCard = Card.playCard(handsOfCards[whichPlayer], lastCard)
    whichPlayer = (whichPlayer + 1) % numberOfPlayers
