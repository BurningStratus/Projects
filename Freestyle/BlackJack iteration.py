import random

deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
        "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,]

hand_dlr = []
hand_plr = []


def value_retrieve(card_s):  # assigns value to "picture" cards
    if card_s == "A":
        return 1
    elif card_s == "K" or card_s == "Q" or card_s == "J":
        return 10
    else:
        pass

def hand_sum(hand_p):  # calcs the sum of cards in hand
    h_sum = 0
    for i in hand_p:
        value_retrieve(i)
        h_sum += i
    return h_sum


def add_card(hand):  # add the card to hand
    rand_indx = random.randint(0, 51)
    # random.shuffle(deck)
    for i in range(1):
        hand.append(deck[rand_indx])
    return None


def show_hands(hand_d, hand_p):
    for i in hand_p:
        print(hand_p[value_retrieve(i)])

    for i in hand_d:
        print(hand_d[value_retrieve(i)])
    return None

#print(value_retrieve('Q'))

user = input("!!!")

add_card(hand_plr)
add_card(hand_plr)
add_card(hand_dlr)
print(hand_plr)
print(hand_dlr)

show_hands(hand_dlr, hand_plr)




while True:
    for i in range(2):
        add_card(hand_plr)
        print("You get a card")

    add_card(hand_dlr)
    show_hands(hand_dlr, hand_plr)

    carder = input("Stay/Hit: ")
    while carder != "Stay":
        if carder == "H":
            add_card(hand_plr)
            show_hands()
            carder = input("Stay/Hit: ")
        else:
            print("prompt not recognized")
            carder = input("Stay/Hit: ")
    print("successful run")
