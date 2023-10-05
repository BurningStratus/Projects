import random
import time
'''
Read comments in order to get a picture of program's command order.

Functions however are NOT ordered.
All of program's most important systems are functions:

1. Take card a.k.a add card(used for dealer and player to take any SINGLE card(means only one))
2//1 Value retriever(value assign for picture cards)
2//2 Sum calc. for all cards in hand(CAUTION! value_retriever is used in sum_calc to get values of pic cards!)
2//3 Ace value calc> if sum(w/out aces) <= 10, ACE == 11, in other cases, ACE == 1 continued>>
2//3 >> for example, if one(dealer or player) gets two aces, first of them will get value of 11, and second will get 1.
3. "show_hands" shows hand of either player or dealer (not obvious: bad naming). So it should be used twice in a row.
4//1. Bet payout is linked with game_state - value. At the each end of game "revolution", continued >>
4//2. game state is either 0, 1, -1. when game is in the process of "revolution" OR a "draw" happened, 
4//3. game_state is 0(though after bet.payout game.state still changes to -1). If player wins the game, game_state is 1. 


'''
deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
play_deck = deck

######################
game_state = 0

eurobucks = int(input("How much money do ya have?: "))  # a.k.a money

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


# value_retrieve and hand_sum are interconnected, since value_retrieve is used in hand_sum
def hand_sum(hand_p):  # calcs the sum of cards in hand
    h_sum = 0          # these are cleared each time function is called
    ace_1_or_11 = 0
    ace_amnt = 0

    for i in hand_p:   # check each card in a hand and uses value_retrieve(refer to value_retrieve to see more)
        value_retrieve(i)
        if value_retrieve(i) > 1:      # for each card that is not ACE, func works normally
            h_sum += value_retrieve(i)
        elif value_retrieve(i) == 1:   # if it encounters ACE, it will count amount of aces =>
            ace_1_or_11 = value_retrieve(i)   # => and store them to deal with a bit later
            ace_amnt += 1

    if ace_1_or_11 != False:           # if there is no aces, prog skips them. False means that there is none (0).
        for i in range(ace_amnt):      # for each ace in hand if there is any
            if h_sum <= 10:             # if sum of cards is less than 10(w/out) aces, ace == 11
                h_sum += 11

                print("i think ace is 11")

            elif h_sum > 10:           # if sum is more than 10, next ace is 1.
                h_sum += 1             # Theoretically, if you get 2 aces, =>

                print("i think ace is 1")

            else:                      # => first of them will be 11, and second will be 1.
                print(i)

    return h_sum
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
#######################################


gamble = input("Wanna gamble? [ENTER]/N: ")

while gamble == "":
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

        for i in range(2):              # gives cards to player
            add_card(hand_plr, play_deck)

            secs = random.uniform(0.5, 1.3)   # little gimmick to give a feeling of dealing the cards
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

            input('\033[32mPress ENTER to continue...\033[0m')  # bloat

            dealer_sum = hand_sum(hand_dlr)
            if dealer_sum < 16:           # kicks in only if dealer has sum < 16
                while dealer_sum < 16:    # Dealer takes cards until he gets at least 16
                    add_card(hand_dlr, play_deck)
                    dealer_sum = hand_sum(hand_dlr)
                    print(f"Dealer:     {show_hands(hand_dlr)}")
                    input('\033[34mDealer takes a card [ENTER]...\033[0m')  # Done for him not to spin too much

            player_sum = hand_sum(hand_plr)  # assign player's sum to var
            dealer_sum = hand_sum(hand_dlr)  # assign dealer's sum to var
            #  each check is coasted to help eyes a little and to slightly improve readability
            #  if both the player and the dealer are busted, dealer's check is b4 player's, so player wins

            if player_sum == 21:                        # from here the game checks conditions of win/lose
                game_state = 1
                print("\033[32mYou win!\033[0m")
                eurobucks = bet_payout(eurobucks, bet)  # this is here to pay out won bet, or to do nothing if lost

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
                game_state = -1                         # workaround to avoid unnecessary bugs and problems
                print("Draw")

            elif player_sum > 21:
                game_state = -1
                print("\033[31mBusted!\033[0m")
                eurobucks = bet_payout(eurobucks, bet)

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
    gamble = input("Play Again? [ENTER]/N:")

    if gamble == "":
        game_state = 0
    else:
        pass
else:
    print("Bye")