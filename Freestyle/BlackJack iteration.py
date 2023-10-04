import random
import time

deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
play_deck = deck

game_state = 0
eurobucks = int(input("How much money do ya have?: "))  # a.k.a money

######################
debt = 3000
######################


######################################
def bet_payout(m_eurobucks, amnt):
    if game_state == 1:
        m_eurobucks = amnt * 2 + m_eurobucks
        return m_eurobucks
    elif game_state == -1:
        return m_eurobucks
    elif game_state == 0:
        m_eurobucks += amnt
        return m_eurobucks


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
# value_retrieve and hand_sum are interconnected, since value_retrieve is used in hand_sum


def add_card(hand, p_deck):  # add the card to hand. Used for dealer and player.
    val = len(p_deck)  # checks how many cards are there in playing deck
    if val > 0:  # if there is at least one, you can take it
        val -= 1
        rand_indx = random.randint(0, val)  # prog just chooses random index of a card.

        time.sleep(1.345)

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
#######################################


gamble = input("Wanna gamble? Y/N: ")

while gamble == "Y":
    if eurobucks <= 0:
        print("You don't have enough money.")
        debt -= -(eurobucks)

    bet = int(input("Enter your bet: "))
    eurobucks -= bet


    print(f"You have {eurobucks}$ in your wallet.\n")

    while game_state == 0:
        game_state = 0  # this one is to track if the game is going, lost or won. 0 = going, 1 = win, -1 = lost

        hand_dlr = []
        hand_plr = []

        for i in range(2):  ## gives cards to player
            add_card(hand_plr, play_deck)
            secs = random.uniform(0.5, 1.3)
            time.sleep(secs)
            print("You get a card")

        add_card(hand_dlr, play_deck)  # gives a card to dealer
        print(f"\nYour cards: {show_hands(hand_plr)}")
        print(f"Dealer:     {show_hands(hand_dlr)}\n")

        carder = input("Stay/Hit: ")      # stay/hit. you can take the whole deck, but no more
        while carder != "S":
            if carder == "H":             # hit. adds card to players hand

                add_card(hand_plr, play_deck)
                print(f"Your cards: {show_hands(hand_plr)}")
                print(f"Dealer:     {show_hands(hand_dlr)}")

                carder = input("Stay/Hit: ")
            else:                          # isn't really needed here, but a good typo-countermeasure.
                print("prompt not recognized")
                carder = input("Stay/Hit: ")
        else:
            print("You choose to stay.")  # when playa' chooses to stay, game moves on to the second part.

            add_card(hand_dlr, play_deck)  # dealer gets second card.
            print(f"Dealer:     {show_hands(hand_dlr)}")

            # input('\033[32mPress ENTER to continue...\033[0m') # bloat

            dealer_sum = hand_sum(hand_dlr)
            if dealer_sum < 16:           # kicks in only if dealer has sum < 16
                while dealer_sum < 16:    # Dealer takes cards until he gets at least 16
                    add_card(hand_dlr, play_deck)
                    dealer_sum = hand_sum(hand_dlr)
                    print(f"Dealer:     {show_hands(hand_dlr)}")
                    input('\033[34mPress ENTER to continue...\033[0m')  # Done for him not to spin too much

            player_sum = hand_sum(hand_plr)  # assign player's sum to var
            dealer_sum = hand_sum(hand_dlr)  # assign dealer's sum to var

            if player_sum == 21:             # from here the game checks conditions of win/lose
                game_state = 1
                print("\033[32mYou win!\033[0m")
                eurobucks = bet_payout(eurobucks, bet)

            elif dealer_sum > 21:
                game_state = 1
                print("\033[32mDealer busted!\033[0m")
                eurobucks = bet_payout(eurobucks, bet)

            elif dealer_sum == 21:
                game_state = -1
                print("\033[31mYou lost!\033[0m")
                eurobucks = bet_payout(eurobucks, bet)

            elif dealer_sum == player_sum:
                game_state = 0
                eurobucks = bet_payout(eurobucks, bet)
                game_state = -1
                print("Draw")

            elif dealer_sum < 21 and player_sum < 21:
                if 21 >= dealer_sum > player_sum:
                    game_state = -1
                    print('\033[31mYou lost!\033[0m')  # red text
                    eurobucks = bet_payout(eurobucks, bet)

                elif 21 >= player_sum > dealer_sum:
                    game_state = 1
                    print("\033[32mYou win!\033[0m")
                    eurobucks = bet_payout(eurobucks, bet)
                else:
                    print("something broke for some reason")
    print(f"You have {eurobucks}$ in your wallet.")
    gamble = input("Play Again? Y/N:")
    if gamble == "Y":
        game_state = 0
    else:
        pass
else:
    print("Bye")