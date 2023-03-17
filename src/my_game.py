import random
from secrets import choice


class Player():
    def __init__(self, name):
        self.name = name

    options = ["rock", "paper", "scissors"]

    hand = ""

    def select(self, the_list, target):
        for x in range(len(the_list)):
            if the_list[x] == target:
                return target
        print("Invald input")
        return -1

    def duel(self, other):
        if self.hand == "rock" and other.hand == "scissors":
            print("\nYou Win!")
        elif self.hand == "rock" and other.hand == "paper":
            print("\nYou lose!")
        elif self.hand == "rock" and other.hand == "rock":
            print("\nDraw!")
        elif self.hand == "paper" and other.hand == "scissors":
            print("\nYou lose!")
        elif self.hand == "paper" and other.hand == "paper":
            print("\nDraw!")
        elif self.hand == "paper" and other.hand == "rock":
            print("\nYou Win!")
        elif self.hand == "scissors" and other.hand == "rock":
            print("\nYou Lose!")
        elif self.hand == "scissors" and other.hand == "paper":
            print("\nYou Win!")
        elif self.hand == "scissors" and other.hand == "scissors":
            print("\nDraw!")


player = Player("Joe")
npc = Player("NPC")


while True:

    response = input("\nDo you want to play rock, paper, scissors? Yes or No ")
    if response == "Yes":
        print("\nAlright, let's play!")
    elif response == "No":
        break

    player_input = input(
        "\nType rock, paper or scisscors to pick what hand you want to play: ")

    player.hand = player.select(player.options, player_input)
    random.shuffle(npc.options)
    npc.hand = random.choice(npc.options)

    print("\nYou have chosen ", player.hand)
    print("\nI have chosen ", npc.hand)

    player.duel(npc)
