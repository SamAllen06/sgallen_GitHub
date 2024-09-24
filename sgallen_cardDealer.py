""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
import random
NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("Clubs", "Hearts", "Spades", "Diamonds")
HANDS = ("Deck", "Player", "Computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        playerHand = [assignCard(cardDB, PLAYER)]
        computerHand = [assignCard(cardDB, COMPUTER)]
        
    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

def initCards():
    """
    No parameters
    create an empty list called cardDB
    Assign 52 entries, all zero
    Return cardDB
    """
    cardDB = []
    for i in range (NUMCARDS):
        cardDB.append(0)
    return cardDB

def showDB(cardDB):
    """
    parameter: cardDB
    Step through all cards
        Print card number
        Print card name getCardName()
        Print card location
    No return value
    """
    print("Deck of Cards")
    for cardNum, location in enumerate(cardDB):
        print (f"{cardNum:3}: {getCardName(cardNum):20} {HANDS[location]}")
    print()

def getCardName(cardNum):
    """
    Parameters: cardNum
    Integer divide cardNum by 13 which goes into “suit”
    Modulus of cardNum and 13 goes into “rank”
    Use SUITNAME and RANKNAME tuples to get a string name
    Return card name
    """
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = f"{RANKNAME[rank]} of {SUITNAME[suit]}"
    return cardName

def assignCard(cardDB, hand):
    """
    Parameters: cardDB, hand
    Pick a random number 0 – 51
    Assign hand to that numbers location
    (how do we make sure same card isn’t picked twice?)
    No return value needed
    """
    keepGoing = True
    while keepGoing:
        cardNum = random.randrange(NUMCARDS)
        if cardDB[cardNum] == 0:
            cardDB[cardNum] = hand
            keepGoing = False
        elif cardDB[cardNum] != 0:
            cardNum = random.randrange(NUMCARDS)

def showHand(cardDB, hand):
    """
    showHand()
    parameters: cardDB, hand
    step through all card
        if card is in hand
            print card name
    No return value
    """
    print(f"Cards in {HANDS[hand]}'s hand")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(f"	{getCardName(cardNum)}")
    print()


main()