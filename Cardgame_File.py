import sys
#Create a Class
class Cards:
    def __init__(self, Suit: str, rank: str ):
        self.suit = Suit
        self.rank = rank
    def __repr__(self) -> str:
        return self.rank + " of " + self.suit
    
    def same_rank(self, other_self)-> bool:
        return self.rank == other_self.rank

    
import random
#For this quick example, 12, 13 are

Hearts2 = Cards("Hearts", "2")
Hearts3 = Cards("Hearts", "3")
Hearts4 = Cards("Hearts", "4")
Hearts5 = Cards("Hearts", "5")
Hearts6 = Cards("Hearts", "6")
Hearts7 = Cards("Hearts", "7")
Hearts8 = Cards("Hearts", "8")
Hearts9 = Cards("Hearts", "9")
Hearts10 = Cards("Hearts", "10")
HeartsJack = Cards("Hearts", "Jack")
HeartsQueen = Cards("Hearts", "Queen")
HeartsKing = Cards("Hearts", "King")
Spades2 = Cards("Spades", "2")
Spades3 = Cards("Spades", "3")
Spades4 = Cards("Spades", "4")
Spades5 = Cards("Spades", "5")
Spades6 = Cards("Spades", "6")
Spades7 = Cards("Spades", "7")
Spades8 = Cards("Spades", "8")
Spades9 = Cards("Spades", "9")
Spades10 = Cards("Spades", "10")
SpadesJack = Cards("Spades", "Jack")
SpadesQueen = Cards("Spades", "Queen")
SpadesKing = Cards("Spades", "King")


# print (Hearts2)

def go(starting: str) -> None:
    Game_start = True

    while Game_start:
            
        Deck = ["Hearts2", "Hearts3", "Hearts4", "Hearts5", "Hearts6", "Hearts7", "Hearts8", "Hearts9", "Hearts10",
        "HeartsJack", "HeartsQueen", "HeartsKing", "Spades2", "Spades3", "Spades4", "Spades5", "Spades6", "Spades7", "Spades8", "Spades9", "Spades10", "SpadesJack",
        "SpadesQueen", "SpadesKing"]

        cards_list = ["Hearts2", "Hearts3", "Hearts4", "Hearts5", "Hearts6", "Hearts7", "Hearts8", "Hearts9", "Hearts10",
        "HeartsJack", "HeartsQueen", "HeartsKing", "Spades2", "Spades3", "Spades4", "Spades5", "Spades6", "Spades7", "Spades8", "Spades9", "Spades10", "SpadesJack",
        "SpadesQueen", "SpadesKing"]

        player1_hand = []

        for cards in range(0,4):
            New_hand = random.choice(Deck)
            Deck.remove(New_hand)
            player1_hand.append(New_hand)

        comp_hand = []

        for card in range(0,4):
            New_hand = random.choice(Deck)
            Deck.remove(New_hand)
            comp_hand.append(New_hand)

        # #def value(ans: list) -> str :
        #     if ans in comp_hand:
        #         return player1_hand.append(ans)
        #     else:
        #         return player1_hand.append(random.choice(Deck))
        def winner_(a : int, b: int) -> int: 
            if a == b:
                print("Draw")
            if a > b:
                print("You win")
            else:
                print("You Lose")

        player1_points = 0
        comp_points = 0
        
        if player1_hand == [None]: 
            print("Computer Won")
            Game_start = False
            break
        if comp_hand == [None]:
            print("You Win")

        choice = input("Type start to start!")
        if choice == "Start" or choice == "start":
            print(f"You're Player 1, Your hand is {player1_hand}")
            print("Game Start")

            comp_turn = True
            Your_turn = True
            
            while Your_turn:
                if player1_points == 3 or comp_points == 3:
                    print(f"Game Over. Your score is: {player1_points} Computer score is: {comp_points}")
                    return Game_start == False

                user_choice = [input("What Card do you want? \n")]
                for card in user_choice:
                    if card in comp_hand:
                        print(f"{card} in comp_hand")
                        Card = comp_hand.index(card)
                        New_Card = comp_hand[Card]
                        comp_hand.remove(New_Card)
                        # if not card in player1_hand: 
                        player1_hand.append(New_Card)
                        print(f"{card} in comp_hand")
                        player1_points+=1
                        print(player1_hand)
                        continue
                    else:
                        print(f"{card} not in comp_hand. Go FISH!")
                        if len(Deck) == 0:
                            print("The Deck is Empty. You cannot go Fish. Game Over")
                            print(f"Your points: {player1_points}, Computers points: {comp_points}")
                            winner_(player1_points, comp_points)
                            return Your_turn == False
                            break
                            
                        else:
                            Card = random.choice(Deck)
                            Deck.remove(Card)
                            if not card in player1_hand: 
                                player1_hand.append(Card)
                                print(player1_hand)
                    while comp_turn:
                        if len(Deck) == 0:
                                print("The Deck is Empty. You cannot go Fish. Game Over")
                                print(f"Your points: {player1_points}, Computers points: {comp_points}")
                                winner_(player1_points, comp_points)
                                return comp_turn == False
                                break
                        else:
                            comp_choice = random.choice(cards_list)
                            if comp_choice in player1_hand:
                                print(f"{comp_choice} in Your hand, You SUCK")
                                Card = player1_hand.index(comp_choice)
                                New_Card = player1_hand[Card]
                                player1_hand.remove(New_Card)
                                comp_hand.append(New_Card)
                                print(f"Comp has taken your card")
                                comp_points+=1 
                                continue
                                # if player1_hand == []:
                                #     print("Game Over")
                                #     Game_start = False
                            else: 
                                print(f"{comp_choice} not in Your hand. Comp, GO FISH!")
                                Card = random.choice(Deck)
                                Deck.remove(Card)
                                comp_hand.append(New_hand)
                                break
        
        elif end_condition(choice):
            print("Game Over")
            return Game_start == False

    if comp_turn == False or Your_turn == False:
        print("Game Over")
        print(f"Your points: {player1_points}, Computers points: {comp_points}")
        winner_(player1_points, comp_points)
        return Game_start == False
        

def end_condition(input: str)-> bool:
    return(input == "q" or input == "quit" or input == "Q" or input == "Quit")

if __name__ == "__main__":
    go(sys.argv)