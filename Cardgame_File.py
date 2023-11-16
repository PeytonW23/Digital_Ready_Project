#Create a Class
class Cards:
    def __init__(self, Suit: str, rank: int ):
        self.suit = Suit
        self.rank = rank
import random
#For this quick example, 12, 13 are

Hearts1 = Cards("Hearts", 1)
Hearts2 = Cards("Hearts", 2)
Hearts3 = Cards("Hearts", 3)
Hearts4 = Cards("Hearts", 4)
Hearts5 = Cards("Hearts", 5)
Hearts6 = Cards("Hearts", 6)
Hearts7 = Cards("Hearts", 7)
Hearts8 = Cards("Hearts", 8)
Hearts9 = Cards("Hearts", 9)
Hearts10 = Cards("Hearts", 10)
Hearts11 = Cards("Hearts", 11)
Hearts12 = Cards("Hearts", 12)
Hearts13 = Cards("Hearts",13)

cards = ["Hearts1", "Hearts2", "Hearts3", "Hearts4", "Hearts5", "Hearts6", "Hearts7", "Hearts8", "Hearts9", "Hearts10", 
         "Spades1", "Spades2", "Spades3", "Spades4", "Spades5", "Spades6", "Spades7", "Spades8", "Spades9", "Spades10"]

hand = ()

for card in range(0,4):
    hand = random.choice(cards)
    print(hand)

#Possible Questions - 
#Do you have a ()
#Do you have a 

# def go(#input):
#         while True: 
#                 for card in range(0,4):
#                 hand = random.choice(cards)
#                 print(hand)
#                 print(input("Ask Question?"))
#                     if y: 
                        #+= 
#                               
                #if end_game():

