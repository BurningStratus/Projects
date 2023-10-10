"""
Black Spade   9824
White Heart   9825
White Diamond 9826
Black Club    9827
"""
'''
import french_cards
from french_cards import x as string
'''
######### storage of values >
cd_suits = {"SPADE": 9824, "HEART": 9825, "DIAMOND": 9826, "CLUB": 9827}
cd_vals = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

deck = {'A♠': 14, 'K♠': 13, 'Q♠': 12, 'J♠': 11,
        '10♠': 10, '9♠': 9, '8♠': 8, '7♠': 7, '6♠': 6, '5♠': 5, '4♠': 4, '3♠': 3, '2♠': 2,
        'A♡': 14, 'K♡': 13, 'Q♡': 12, 'J♡': 11,
        '10♡': 10, '9♡': 9, '8♡': 8, '7♡': 7, '6♡': 6, '5♡': 5, '4♡': 4, '3♡': 3, '2♡': 2,
        'A♢': 14, 'K♢': 13, 'Q♢': 12, 'J♢': 11,
        '10♢': 10, '9♢': 9, '8♢': 8, '7♢': 7, '6♢': 6, '5♢': 5, '4♢': 4, '3♢': 3, '2♢': 2,
        'A♣': 14, 'K♣': 13, 'Q♣': 12, 'J♣': 11,
        '10♣': 10, '9♣': 9, '8♣': 8, '7♣': 7, '6♣': 6, '5♣': 5, '4♣': 4, '3♣': 3, '2♣': 2}
######### end of storage    <


def value_retrieve(card_s):  # assigns value to "picture" cards
    if card_s == "A":
        return 14
    elif card_s == "K":
        return 13
    elif card_s == "Q":
        return 12
    elif card_s == "J":
        return 11
    else:
        return int(card_s)

'''
for suits in cd_suits:
    print(suits)
    for cards in cd_vals:

        cd_value = value_retrieve(cards)

        suit_ansi = int(cd_suits[suits])        # get ascii code of suit
        card_suit = str(chr(suit_ansi))         # print suit in ascii
        cards = str(cards)
        dict_key = cards + card_suit
        deck[dict_key] = cd_value

    print(f"{suits} DONE")
'''
for inner in range(4):
    for outer in range(2, 14):
        print(deck[outer])


