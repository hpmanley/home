import random
import json
import os

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        if self.rank == "Joker":
            return "Joker"
        else:
            return str(self.rank) + " of " + str(self.suit)

def get_card_val(c):
    # returns how much the card is worth
    r = c.rank
    if r == "2":
        val = 2
    if r == "3":
        val = 3
    if r == "4":
        val = 4
    if r == "5":
        val = 5
    if r == "6":
        val = 6
    if r == "7":
        val = 7
    if r == "8":
        val = 8
    if r == "9":
        val = 9
    if r == "10":
        val = 10
    if r == "J":
        val = 11
    if r == "Q":
        val = 12
    if r == "K":
        val = 13
    if r == "A":
        val = 14
    if r == "Joker":
        val = 0
    return val

# making the deck
the_deck = []

# hearts first
the_deck.append(Card("2", "Hearts"))
the_deck.append(Card("3", "Hearts"))
the_deck.append(Card("4", "Hearts"))
the_deck.append(Card("5", "Hearts"))
the_deck.append(Card("6", "Hearts"))
the_deck.append(Card("7", "Hearts"))
the_deck.append(Card("8", "Hearts"))
the_deck.append(Card("9", "Hearts"))
the_deck.append(Card("10", "Hearts"))
the_deck.append(Card("J", "Hearts"))
the_deck.append(Card("Q", "Hearts"))
the_deck.append(Card("K", "Hearts"))
the_deck.append(Card("A", "Hearts"))

# diamonds
the_deck.append(Card("2", "Diamonds"))
the_deck.append(Card("3", "Diamonds"))
the_deck.append(Card("4", "Diamonds"))
the_deck.append(Card("5", "Diamonds"))
the_deck.append(Card("6", "Diamonds"))
the_deck.append(Card("7", "Diamonds"))
the_deck.append(Card("8", "Diamonds"))
the_deck.append(Card("9", "Diamonds"))
the_deck.append(Card("10", "Diamonds"))
the_deck.append(Card("J", "Diamonds"))
the_deck.append(Card("Q", "Diamonds"))
the_deck.append(Card("K", "Diamonds"))
the_deck.append(Card("A", "Diamonds"))

# clubs
the_deck.append(Card("2", "Clubs"))
the_deck.append(Card("3", "Clubs"))
the_deck.append(Card("4", "Clubs"))
the_deck.append(Card("5", "Clubs"))
the_deck.append(Card("6", "Clubs"))
the_deck.append(Card("7", "Clubs"))
the_deck.append(Card("8", "Clubs"))
the_deck.append(Card("9", "Clubs"))
the_deck.append(Card("10", "Clubs"))
the_deck.append(Card("J", "Clubs"))
the_deck.append(Card("Q", "Clubs"))
the_deck.append(Card("K", "Clubs"))
the_deck.append(Card("A", "Clubs"))

# spades
the_deck.append(Card("2", "Spades"))
the_deck.append(Card("3", "Spades"))
the_deck.append(Card("4", "Spades"))
the_deck.append(Card("5", "Spades"))
the_deck.append(Card("6", "Spades"))
the_deck.append(Card("7", "Spades"))
the_deck.append(Card("8", "Spades"))
the_deck.append(Card("9", "Spades"))
the_deck.append(Card("10", "Spades"))
the_deck.append(Card("J", "Spades"))
the_deck.append(Card("Q", "Spades"))
the_deck.append(Card("K", "Spades"))
the_deck.append(Card("A", "Spades"))

# the jokers
the_deck.append(Card("Joker", None))
the_deck.append(Card("Joker", None))

name1 = ""
name2 = ""
hand1 = []
hand2 = []
score1 = 0
score2 = 0
current_round = 0
total_rounds = 0

print("=" * 50)
print("WELCOME TO CARD WAR!!!")
print("=" * 50)
print("")

menu = input("type n for new game or l to load a save: ")

if menu == "l" or menu == "L":
    fname = input("what file? (just hit enter for game_save.json): ")
    if fname == "":
        fname = "game_save.json"
    
    try:
        f = open(fname, "r")
        stuff = json.load(f)
        f.close()
        
        name1 = stuff["p1"]["name"]
        name2 = stuff["p2"]["name"]
        score1 = stuff["p1"]["score"]
        score2 = stuff["p2"]["score"]
        current_round = stuff["round"]
        total_rounds = stuff["total"]
        
        for card_info in stuff["p1"]["cards"]:
            hand1.append(Card(card_info[0], card_info[1]))
        
        for card_info in stuff["p2"]["cards"]:
            hand2.append(Card(card_info[0], card_info[1]))
        
        print("loaded!")
    except:
        print("couldnt load that file, making new game")
        menu = "n"

if menu == "n" or menu == "N" or menu == "":
    name1 = input("player 1 name: ")
    if name1 == "":
        name1 = "Player 1"
    
    name2 = input("player 2 name: ")
    if name2 == "":
        name2 = "Player 2"
    
    # get rounds
    got_rounds = False
    while got_rounds == False:
        try:
            rounds_input = input("how many rounds? ")
            total_rounds = int(rounds_input)
            if total_rounds > 0:
                got_rounds = True
        except:
            print("enter a number please")
    
    # shuffle and deal
    random.shuffle(the_deck)
    
    middle_point = len(the_deck) // 2
    hand1 = the_deck[:middle_point]
    hand2 = the_deck[middle_point:]
    
    score1 = 0
    score2 = 0
    current_round = 0

print("")
print("Game setup:")
print(name1 + " vs " + name2)
print("playing " + str(total_rounds) + " rounds")
print("")

# the actual game
keep_playing = True

while keep_playing == True:
    if current_round >= total_rounds:
        break
    
    choice = input("(p)lay, (s)ave, or (q)uit? ")
    
    if choice == "q" or choice == "Q":
        print("ok bye")
        keep_playing = False
        break
    
    if choice == "s" or choice == "S":
        savename = input("filename to save as: ")
        if savename == "":
            savename = "game_save.json"
        
        # gotta convert the cards
        cards1_to_save = []
        for card in hand1:
            cards1_to_save.append([card.rank, card.suit])
        
        cards2_to_save = []
        for card in hand2:
            cards2_to_save.append([card.rank, card.suit])
        
        savedata = {}
        savedata["p1"] = {}
        savedata["p1"]["name"] = name1
        savedata["p1"]["cards"] = cards1_to_save
        savedata["p1"]["score"] = score1
        savedata["p2"] = {}
        savedata["p2"]["name"] = name2
        savedata["p2"]["cards"] = cards2_to_save
        savedata["p2"]["score"] = score2
        savedata["round"] = current_round
        savedata["total"] = total_rounds
        
        f = open(savename, "w")
        json.dump(savedata, f)
        f.close()
        
        print("saved as " + savename)
        print("")
        
    if choice == "p" or choice == "P":
        current_round = current_round + 1
        
        print("")
        print("--- ROUND " + str(current_round) + " ---")
        
        # draw cards
        card1 = None
        card2 = None
        
        if len(hand1) > 0:
            card1 = hand1[0]
            hand1.remove(card1)
        
        if len(hand2) > 0:
            card2 = hand2[0]
            hand2.remove(card2)
        
        print(name1 + " plays: " + str(card1))
        print(name2 + " plays: " + str(card2))
        
        # cards on the table
        cards_in_play = []
        if card1 != None:
            cards_in_play.append(card1)
        if card2 != None:
            cards_in_play.append(card2)
        
        # special card stuff
        # ace of hearts = extra turn
        if card1 != None:
            if card1.rank == "A":
                if card1.suit == "Hearts":
                    print("!!! " + name1 + " got Ace of Hearts! Extra turn!")
                    if len(hand1) > 0:
                        extra1 = hand1[0]
                        hand1.remove(extra1)
                        print(name1 + " draws " + str(extra1))
                        cards_in_play.append(extra1)
                        
                        if extra1.rank == "Joker":
                            print("JOKER!!! SCORES GO BACK TO ZERO!")
                            score1 = 0
                            score2 = 0
        
        if card2 != None:
            if card2.rank == "A":
                if card2.suit == "Hearts":
                    print("!!! " + name2 + " got Ace of Hearts! Extra turn!")
                    if len(hand2) > 0:
                        extra2 = hand2[0]
                        hand2.remove(extra2)
                        print(name2 + " draws " + str(extra2))
                        cards_in_play.append(extra2)
                        
                        if extra2.rank == "Joker":
                            print("JOKER!!! SCORES GO BACK TO ZERO!")
                            score1 = 0
                            score2 = 0
        
        # joker resets everything
        if card1 != None:
            if card1.rank == "Joker":
                print("JOKER!!! SCORES GO BACK TO ZERO!")
                score1 = 0
                score2 = 0
        
        if card2 != None:
            if card2.rank == "Joker":
                print("JOKER!!! SCORES GO BACK TO ZERO!")
                score1 = 0
                score2 = 0
        
        # who wins?
        if card1 == None and card2 == None:
            print("nobody has cards")
            keep_playing = False
        elif card1 == None:
            print(name2 + " wins (other player out of cards)")
            score2 = score2 + 1
            for c in cards_in_play:
                hand2.append(c)
        elif card2 == None:
            print(name1 + " wins (other player out of cards)")
            score1 = score1 + 1
            for c in cards_in_play:
                hand1.append(c)
        else:
            value1 = get_card_val(card1)
            value2 = get_card_val(card2)
            
            if value1 > value2:
                print(name1 + " wins!")
                score1 = score1 + 1
                for c in cards_in_play:
                    hand1.append(c)
            elif value2 > value1:
                print(name2 + " wins!")
                score2 = score2 + 1
                for c in cards_in_play:
                    hand2.append(c)
            else:
                print("tie, cards thrown out")
        
        print("")
        print(name1 + ": " + str(score1) + " points, " + str(len(hand1)) + " cards")
        print(name2 + ": " + str(score2) + " points, " + str(len(hand2)) + " cards")
        print("")
        
        if len(hand1) == 0 and len(hand2) == 0:
            print("everyone is out of cards")
            keep_playing = False

# game over
print("")
print("=" * 50)
print("GAME OVER")
print("=" * 50)
print("")
print("Final scores:")
print(name1 + ": " + str(score1))
print(name2 + ": " + str(score2))
print("")

if score1 > score2:
    print(name1 + " WINS!!!")
elif score2 > score1:
    print(name2 + " WINS!!!")
else:
    print("its a tie!")

print("")
print("thanks for playing my game")
