import Card
import os

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(cardStack)
                    ,Card.initHand(cardStack), Card.initHand(cardStack)]
whichPlayer = 0
#direction 1: clockwise, 0: counter-clockwise
direction = 1
while Card.someoneWon(handsOfCards) == False:
    os.system("cls" if os.name == "nt" else "clear")
    Card.showCurrentScreen(handsOfCards[whichPlayer],direction)
    Card.playCard(handsOfCards[whichPlayer])
    whichPlayer = (whichPlayer + 1) % numberOfPlayers
