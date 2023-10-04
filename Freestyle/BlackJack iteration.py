import random


deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

play_deck = deck

#################################
def value_retrieve(card_s):  # assigns value to "picture" cards
    if card_s == "K" or card_s == "Q" or card_s == "J":
        return 10
    elif card_s == "A":
        return 1
    else:
        return int(card_s)


def hand_sum(hand_p):  # calcs the sum of cards in hand
    h_sum = 0
    for i in hand_p:
        h_sum += value_retrieve(i)

    return h_sum
#################################
# value_retrieve and hand_sum are interconnected, since value_retrieve is used in hand_sum


def add_card(hand, p_deck):  # add the card to hand. Used for dealer and player.
    val = len(p_deck)  # checks how many cards are there in playing deck
    if val > 0:  # if there is at least one, you can take it
        val -= 1
        rand_indx = random.randint(0, val)  # prog just chooses random index of a card.
        hand.append(deck[rand_indx])
        p_deck.remove(p_deck[rand_indx])
    else:
        print("Deck is empty. Are you insane?")
    return None


def show_hands(hand):
    crds = ""
    for i in hand:
        crds += str(i) + " "

    return crds


while not False:

        game_state = 0  # this one is to track if the game is going, lost or won. 0 = going, 1 = win, -1 = lost

        hand_dlr = []
        hand_plr = []

        for i in range(2):  ## gives cards to player
            add_card(hand_plr, play_deck)
            print("You get a card")

        add_card(hand_dlr, play_deck)  # gives a card to dealer
        print(f"Your cards: {show_hands(hand_plr)}")
        print(f"Dealer:     {show_hands(hand_dlr)}")

        print(len(play_deck))

        carder = input("Stay/Hit: ")      # stay/hit. you can take the whole deck, but no more
        while carder != "S"
            if carder == "H":

                add_card(hand_plr, play_deck)
                print(f"Your cards: {show_hands(hand_plr)}")
                print(f"Dealer:     {show_hands(hand_dlr)}")

                print(len(play_deck))

                carder = input("Stay/Hit: ")
            else:
                print("prompt not recognized")
                carder = input("Stay/Hit: ")
        else:
            print("You choose to stay.")  # when playa' chooses to stay, game moves on to the second part

            add_card(hand_dlr, play_deck)
            show_hands(hand_dlr)

            input('\033[32mPress Enter to continue...\033[0m')

            dealer_sum = hand_sum(hand_dlr)
            if dealer_sum < 16:           # kicks in only if dealer has sum < 16
                while dealer_sum < 16:    # Dealer takes cards until he gets at least 16
                    add_card(hand_dlr, play_deck)
                    dealer_sum = hand_sum(hand_dlr)
                    print(dealer_sum)
                    input('\033[32mPress Enter to continue...\033[0m')  # Done for him not to spin too much

            player_sum = hand_sum(hand_plr)  # assign player's sum to var
            dealer_sum = hand_sum(hand_dlr)  # assign dealer's sum to var

            if player_sum > 21:  # busted!
                game_state = -1
                print("Busted!")
            elif dealer_sum > 21:
                game_state = 1
                print("Win!")
