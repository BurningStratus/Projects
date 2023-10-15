###### imports
import random
import time
from french_cards import return_hearts as r_ht
from french_cards import return_diamonds as r_dm
from french_cards import return_clubs as r_cl
from french_cards import return_spades as r_sp
###### end of imports
"""
Black Spade   9824 == 
White Heart   9825
White Diamond 9826
Black Club    9827
"""
'''
TODO PRIMARY OBJECTIVE: teach computer to evaluate cards with different suits and take Trumps into account.
TODO PRIMARY OBJECTIVE: add cards to table

DONE trump suited cards change values also in hands of the players.
DONE consider if other file is needed for cards: yes, we don't really need it. 
DONE show trumps as usual cards DONE

TODO SECONDARY: show 14, 13, 12, 11 as A, K, Q, J
'''
######### storage of values >
cd_suits = {"SPADE": 9824, "HEART": 9825, "DIAMOND": 9826, "CLUB": 9827}
cd_vals = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
''' courier's stash

to create list of cards: 
for suits in cd_suits:
    print(suits)
    for cards in cd_vals:

        #cd_value = value_retrieve(cards)

        suit_ansi = int(cd_suits[suits])        # get ascii code of suit
        card_suit = str(suit_ansi)              # print suit in ascii
        cards = str(cards)
        dict_key = cards + card_suit
        #deck_list[dict_key] = cd_value
        deck_list.append(dict_key)

    print(f"{suits} DONE")

print(deck_list)

to create lists:
for i in deck:
    new_code = 0
    
    if "14" in i:
        mod = str(14)  # A is 14xxxx now
        i_mod = i[1:]
        new_code = mod + i_mod
    elif "13" in i:
        mod = str(13)  # K is 13xxxx now
        i_mod = i[1:]
        new_code = mod + i_mod
    elif "12" in i:
        mod = str(12)  # Q is 12xxxx now
        i_mod = i[1:]
        new_code = mod + i_mod
    elif "11" in i:
        mod = str(11)  # J is 11xxxx now
        i_mod = i[1:]
        new_code = mod + i_mod
    elif "10" in i:
        mod = str(10)
        i_mod = i[1:]
        new_code = mod + i_mod
    else:
        f_lttr = str(0) + i[0]
        rest_lttrs = i[1:]
        new_code = f_lttr + rest_lttrs

    deck_listmod.append(new_code)

print(deck_listmod)

for refactoring: 
for i in deck:
    if "9824" in i:
        mod = i[0:2]  # i is xx01 now
        i_mod = "01"
        new_code = mod + i_mod
    elif "9825" in i:
        mod = i[0:2]  # i is xx02 now
        i_mod = "02"
        new_code = mod + i_mod
    elif "9826" in i:
        mod = i[0:2]  # i is xx03 now
        i_mod = "03"
        new_code = mod + i_mod
    elif "9827" in i:
        mod = i[0:2]  # i is xx04 now
        i_mod = "04"
        new_code = mod + i_mod
    deck_nw.append(new_code)
    print(f"Card processed.{new_code}")
print(deck_nw)


different types of decks:
deck_NOTu = {'A♠': 14, 'K♠': 13, 'Q♠': 12, 'J♠': 11,
        '10♠': 10, '9♠': 9, '8♠': 8, '7♠': 7, '6♠': 6, '5♠': 5, '4♠': 4, '3♠': 3, '2♠': 2,
        'A♡': 14, 'K♡': 13, 'Q♡': 12, 'J♡': 11,
        '10♡': 10, '9♡': 9, '8♡': 8, '7♡': 7, '6♡': 6, '5♡': 5, '4♡': 4, '3♡': 3, '2♡': 2,
        'A♢': 14, 'K♢': 13, 'Q♢': 12, 'J♢': 11,
        '10♢': 10, '9♢': 9, '8♢': 8, '7♢': 7, '6♢': 6, '5♢': 5, '4♢': 4, '3♢': 3, '2♢': 2,
        'A♣': 14, 'K♣': 13, 'Q♣': 12, 'J♣': 11,
        '10♣': 10, '9♣': 9, '8♣': 8, '7♣': 7, '6♣': 6, '5♣': 5, '4♣': 4, '3♣': 3, '2♣': 2}

deck_NOTu1 = {'A9824': 14, 'K9824': 13, 'Q9824': 12, 'J9824': 11, '109824': 10, '99824': 9, '89824': 8, '79824': 7,
                '69824': 6, '59824': 5, '49824': 4, '39824': 3, '29824': 2, 'A9825': 14, 'K9825': 13, 'Q9825': 12,
                'J9825': 11, '109825': 10, '99825': 9, '89825': 8, '79825': 7, '69825': 6, '59825': 5, '49825': 4,
                '39825': 3, '29825': 2, 'A9826': 14, 'K9826': 13, 'Q9826': 12, 'J9826': 11, '109826': 10, '99826': 9,
                '89826': 8, '79826': 7, '69826': 6, '59826': 5, '49826': 4, '39826': 3, '29826': 2, 'A9827': 14,
                'K9827': 13, 'Q9827': 12, 'J9827': 11, '109827': 10, '99827': 9, '89827': 8, '79827': 7, '69827': 6,
                '59827': 5, '49827': 4, '39827': 3, '29827': 2}

deck_NOTu2 = ['A9824', 'K9824', 'Q9824', 'J9824', '19824', '99824', '89824', '79824', '69824', '59824', '49824',
             '39824', '29824', 'A9825', 'K9825', 'Q9825', 'J9825', '19825', '99825', '89825', '79825', '69825',
             '59825', '49825', '39825', '29825', 'A9826', 'K9826', 'Q9826', 'J9826', '19826', '99826', '89826',
             '79826', '69826', '59826', '49826', '39826', '29826', 'A9827', 'K9827', 'Q9827', 'J9827', '19827',
             '99827', '89827', '79827', '69827', '59827', '49827', '39827', '29827']

deck_NOTu3 = ['149824', '139824', '129824', '119824', '109824', '099824', '089824', '079824',
        '069824', '059824', '049824', '039824', '029824', '149825', '139825', '129825',
        '119825', '109825', '099825', '089825', '079825', '069825', '059825', '049825',
        '039825', '029825', '149826', '139826', '129826', '119826', '109826', '099826',
        '089826', '079826', '069826', '059826', '049826', '039826', '029826', '149827',
        '139827', '129827', '119827', '109827', '099827', '089827', '079827', '069827',
        '059827', '049827', '039827', '029827']
'''

deck = ['1401', '1301', '1201', '1101',
        '1001', '0901', '0801', '0701',
        '0601', '0501', '0401', '0301',
        '0201', '1402', '1302', '1202',
        '1102', '1002', '0902', '0802',
        '0702', '0602', '0502', '0402',
        '0302', '0202', '1403', '1303',
        '1203', '1103', '1003', '0903',
        '0803', '0703', '0603', '0503',
        '0403', '0303', '0203', '1404',
        '1304', '1204', '1104', '1004',
        '0904', '0804', '0704', '0604',
        '0504', '0404', '0304', '0204']     ### original deck. card example::  1402: [14] is card's value(ACE), [02] is suit(HEARTS).
deck_translate = {"A": "14", "K": "13", "Q": "12", "J": "11"}
play_deck = []   ### used for game
table = dict()   ### playing table
table_dump = []  ### dump

trump_card = []  ### trump card

player_hand = []
bot_hand = []


######### end of storage    <


######### functions


def value_retrieve(card) -> int:
    # assigns value to cards for calculations.
    if card[0] == "0":
        card_value = int(card[1])
        return card_value
    else:
        card_value = int(str(card[0] + card[1]))  # 1 + 2 = str(12) ==> int(12) = 12.
        return card_value

# def card_translate(card) -> int:
#     if len(card) == 3:
#
#     elif len(card) == 4:
#
#     return


def add_card(hand) -> None:
    # add the card to hand.
    pl_deck = play_deck
    cards_in_deck = len(pl_deck)  # checks how many cards are there in playing deck

    if cards_in_deck > 0:  # if there is any, card can be taken
        cards_in_deck -= 1
        rand_indx = random.randint(0, cards_in_deck)  # prog just chooses random index of a card.
        hand.append(pl_deck[rand_indx])
        pl_deck.remove(pl_deck[rand_indx])

        # print(f"{cards_in_deck} cards in deck.")

    else:
        print("None in the deck.")
    return None


def add_to_table(card):

    return


def show_picture(card) -> str:  # show picture and show hand are interconnected.
    if card[2:] == "01":  # shows hearts
        picture = r_ht()  # calls func from another file
        return picture
    elif card[2:] == "02":  # shows diamonds
        picture = r_dm()
        return picture
    elif card[2:] == "03":  # shows clubs
        picture = r_cl()
        return picture
    elif card[2:] == "04":  # shows spades
        picture = r_sp()
        return picture
    else:
        print("fuck you")


def show_hand(hand, player) -> str:  # should be inserted into print to show return value. print(show_hand)
    string_to_show = ''              # 1 == player or table, 0 == opponent
    show = ''                        # if player, cards are shown with their values. If opponent, them cards are covered.
    covered_card = chr(9632)

    if player == 1:
        for playing_card in hand:
            if playing_card[0] == "0":
                show = str(playing_card[1])
            elif playing_card[0] == "2":
                show = str(int(playing_card[0:2]) - 20)
            elif playing_card[0] == "1":
                show = str(playing_card[0] + playing_card[1])  # 1 + 2 = str(12) ==> int(12) = 12.
            elif playing_card[0] == "3":
                show = str(int(playing_card[0] + playing_card[1]) - 20)

            card = show_picture(playing_card) + show  # calls show picture func to get picture in ASCII
            string_to_show += ' ' + card
        return string_to_show
    elif player == 0:
        for playing_card in hand:
            string_to_show += " " + covered_card

        return string_to_show
    else:
        print("something broke for some reason")
        return "err"


def card_comparator():

    return


def create_trump(trump_c, pl_deck) -> None:            # makes up trump suit and card.
    pl_deck = play_deck

    rand_indx = random.randint(0, len(pl_deck))   # 1. prog chooses random index of a card
    trump_c.append(pl_deck[rand_indx])                # 2. trump is added in its own list
    pl_deck.remove(pl_deck[rand_indx])                # 3. chosen card is removed from the play_deck

    print(f"creating trumps deck ...")
    trumpcreation_iterator(pl_deck)
    print(f"creating trumps player hand ...")
    trumpcreation_iterator(player_hand)
    print(f"creating trumps opponent hand ...")
    trumpcreation_iterator(bot_hand)
    return None


### trumpcreation iterator is used for iteration over a list. Bot hand, player hand and play_deck to make trumps.
### trumpcreation is used inside create_trump function.
def trumpcreation_iterator(iterable):
    # print(f"trumpeting \n{iterable}")
    for all_cards in iterable[0:len(iterable)-1]:
        # for all cards in list with original value.
        # if removed, some cards will be changed several times
        # if len() is removed, if card already got value of 33, it will get 53 and eventually 73.
        trumpet = trump_card[0]   # goes to trump card list and gets trump suit from there

        if all_cards[2:] == trumpet[2:]:
            # if suit is the same as trump card's, the card will get trump value (+20).
            print(f"found card for trumping: {all_cards}")
            memory_value = int(all_cards[0:2]) + 20           # chosen card's value + 20
            memory_value = str(memory_value) + all_cards[2:]  # suit is added

            iterable.remove(all_cards)                          # remove old card
            iterable.append(memory_value)                       # add new value
            print(f"value changed to: {memory_value}\n")
    return iterable

######### end of functions


# play_deck.extend(deck)
#
# add_card(player_hand)
# print(f" Your cards: {show_hand(player_hand)}")
# print(player_hand)


######### game itself
while True:
    spinner = 1
    play_deck.extend(deck)

    #  print(play_deck)

    for cards_for_start in range(12):
        if spinner % 2 == 0:

            rand_sec = random.uniform(0.4, 0.9)
            time.sleep(rand_sec)

            add_card(player_hand)
            print("You get a card")
            spinner += 1
        else:

            rand_sec = random.uniform(0.4, 0.9)
            time.sleep(rand_sec)

            add_card(bot_hand)
            print("Opponent gets a card\n")
            spinner += 1

    create_trump(trump_card, play_deck)

    print(f"Your hand: {show_hand(player_hand, 1)}\n")
    print(f"Opponent:  {show_hand(bot_hand, 0)}\n")
    print(f"Table:     {show_hand(table, 1)}       {show_hand(trump_card, 1)}")

    print(show_hand(table, 1))
    # print(len(play_deck))

    input('\033[32mPress ENTER to continue...\033[0m')

    # simplified. Player always goes first. should be changed.

    carder = input("ADD(3HT, ACL, ASP ... ):>")

    if len(carder) == 3:
        pass
    elif len(carder) == 4:
        pass

else:
    pass
######### end o' game
