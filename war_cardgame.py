class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return "I am {}. I have this set of cards {}".format(self.name, self.hand)

    def add_card(self, card):
        if card != None:
            self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def hand_size(self):
        return len(self.hand)


import random


class CardDeck:
    def __init__(self):
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"

        self.deck = (
            hearts.split(",")
            + diamonds.split(",")
            + spades.split(",")
            + clubs.split(",")
        )

    def get_card(self):
        if len(self.deck) == 0:
            return None

        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def give_higher(self, card1, card2):
        if card1[0] > card2[0]:
            return card1

        elif card1[0] < card2[0]:
            return card2

        elif card1[1] > card2[1]:
            return card1

        else:
            return card2


name1 = input("whats your name, player1 :")
player1 = Player(name1)
name2 = input("whats your name, player2 :")
player2 = Player(name2)
deck = CardDeck()

round = 0

while True:
    round = round + 1

    player1_card = deck.get_card()
    player1.add_card(player1_card)

    player2_card = deck.get_card()
    player2.add_card(player2_card)

    if player1_card == None or player2_card == None:
        print("Game Over. No more cards in deck.")
        print(name1, " has ", player1.hand_size())
        print(name2, " has ", player2.hand_size())
        print("Who won?")

        if player1.hand_size() > player2.hand_size():
            print(name2, "wins. They played", round, "rounds.")

        elif player1.hand_size() < player2.hand_size():
            print(name1, "wins. They played ", round, "rounds.")

        else:
            print("TIE!!!!!!. They played ", round, "rounds.")

        break

    else:
        if deck.give_higher(player1_card, player2_card) == player1_card:
            player2.add_card(player1_card)
            player1.remove_card(player1_card)
            print(name1, "gives", player1_card, "to", name2)

        else:
            player1.add_card(player2_card)
            player2.remove_card(player2_card)
            print(name2, "gives", player2_card, "to", name1)
