import Card
import os

cardStack = Card.initStackOfCards()
Card.shuffleDeckofCards(cardStack)
numberOfPlayers = int(input("How many players? "))
handsOfCards = [Card.initHand(cardStack), Card.initHand(cardStack)
                    ,Card.initHand(cardStack), Card.initHand(cardStack)]
i = 0
#direction 1: clockwise, 0: counter-clockwise
direction = 1
while Card.someoneWon(handsOfCards) == False:
    os.system("cls" if os.name == "nt" else "clear")
    Card.showCurrentScreen(handsOfCards[i],direction)
    Card.playCard(handsOfCard[i])
    i+=1
