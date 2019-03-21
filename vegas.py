from rit_lib import *
from myStack import *
from myQueue import *
from myNode import *
import random
"""
Vegas - Brandon Calabrese

You can toggle 'debug' to see how each game plays out

NOTE- To simulate a properly sorted deck, the deck is sorted every
time the player draws a card.
"""

"""Shows the game playing out as it is processed, explains the results of the simulation"""
debug = False
def debugMessage(text):
    if debug == True:
        print(text)

"""Shuffled given deck by moving top card to bottom random number of times"""
def shuffle(deck):
    for i in range(random.randint(0,deck.size - 1)):
        card = front(deck)
        dequeue(deck)
        enqueue(deck,card)
    return deck

"""Generates deck of cards of a certain size, also randomly sorted."""
def generateDeck(deckSize):
    deck = createQueue()
    counter = 0
    while counter < deckSize:
        enqueue(deck,counter + 1)
        counter += 1
    deck = shuffle(deck)
    return deck


"""Determines which discard pile to send card"""
def discardCard(card, stack1, stack2):
    """Places card in empty pile if possible"""
    if stack1.size == 0:
        push(stack1, card)
        debugMessage("Discarded " + str(card.data) + " to pile 1")
    elif card.data < top(stack1).data:
        push(stack1, card)
        debugMessage("Discarded " + str(card.data) + " to pile 1")
    elif stack2.size == 0:
        push(stack2, card)
        debugMessage("Discarded " + str(card.data) + " to pile 2")
    else:
        """Chooses pile if card value is one less than top of pile"""
        if top(stack1) == card.data - 1:
            push(stack1, card)
            debugMessage("Discarded " + str(card.data) + " to pile 1")
        elif top(stack2) == card.data - 1:
            push(stack2, card)
            debugMessage("Discarded " + str(card.data) + " to pile 2")
        else:
            """Worse case scenario, mush choose which stack to cut off"""
            if top(stack1).data > top(stack2).data:
                push(stack1, card)
                debugMessage("Discarded " + str(card.data) + " to pile 1")
            else:
                push(stack2, card)
                debugMessage("Discarded " + str(card.data) + " to pile 2")

"""Simulates the game defined on the lab sheet"""
def simulateGame(deckSize):
    debugMessage("")
    victoryPile = createStack()
    discardPile1 = createStack()
    discardPile2 = createStack()

    deck = generateDeck(deckSize)
    
    oldDeckSize = deck.size
    
    while True:            
        """Determines where to put top card in deck"""
        if deck.size > 0:
            debugMessage("Top deck card: " + str(front(deck)))
            if victoryPile.size > 0:
                if front(deck) == top(victoryPile).data + 1:
                    debugMessage("Found card #" + str(front(deck)))
                    push(victoryPile, deck.front)
                else:
                    """Adds card to one of the discard piles"""
                    discardCard(deck.front, discardPile1, discardPile2)                     
            else:
                """For when card #1 comes up"""
                if front(deck) == 1:
                    push(victoryPile, deck.front)
                    debugMessage("Found card #1")
                else:
                    """Adds card to one of the discard piles"""
                    discardCard(deck.front, discardPile1, discardPile2)
            dequeue(deck)

        oldPileSize1 = discardPile1.size
        oldPileSize2 = discardPile2.size
        
        """Checks if possible to add cards from discard to victory"""
        while True:
            if victoryPile.size == 0:
                break
            
            c1 = False
            c2 = False
            
            """Checks if can take top card from discard 1"""
            if discardPile1.size > 0:
                if top(discardPile1).data == top(victoryPile).data + 1:
                    debugMessage("Found card #" + str(discardPile1.top.data.data) + " from pile 1")
                    push(victoryPile, top(discardPile1))
                    pop(discardPile1)
                    c1 = True
            """Checks if can take top card from discard 2"""
            if discardPile2.size > 0:
                if top(discardPile2).data == top(victoryPile).data + 1:
                    debugMessage("Found card #" + str(discardPile2.top.data.data) + " from pile 2")
                    push(victoryPile, top(discardPile2))
                    pop(discardPile2)
                    c2 = True
            """If no cards can be added to victory stack then break"""
            if c1 == False and c2 == False:
                break
            
        if deck.size == 0:
            if victoryPile.size == deckSize:
                break
            if oldPileSize1 == discardPile1.size and oldPileSize2 == discardPile2.size:
                break
        else:
            """Shuffles deck before each card pull to keep deck trully random"""
            if deck.size < oldDeckSize:
                deck = shuffle(deck)
        
    debugMessage("Game Results: " + str(victoryPile.size)) 
    return victoryPile

"""Gets user input, calls simulation function, and outputs the results of the simulation"""
def main():
    print("Welcome to Vegas!")
    deckSize = int(input("Input deck size: "))
    gameNum = int(input("Input number of games: "))
    
    avgVictoryNum = 0
    maxVictoryNum = 0
    minVictoryNum = deckSize
    
    
    counter = 0
    while counter < gameNum:
        deck = simulateGame(deckSize)
        avgVictoryNum += deck.size
        if deck.size > maxVictoryNum:
            maxVictoryNum = deck.size
        if deck.size < minVictoryNum:
            minVictoryNum = deck.size
        counter += 1
        
    avgVictoryNum /= gameNum
    print("Average Victory Pile Size: " + str(avgVictoryNum))
    print("Maximum Victory Pile Size: " + str(maxVictoryNum))
    print("Minimum Victory Pile Size: " + str(minVictoryNum))
    
main()
