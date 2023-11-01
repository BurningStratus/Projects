import random

print("""
 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌      ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌       ▐░▌         ▐░▌  ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌        ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌         ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌    ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌          ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌            ▐░▌▐░▌       ▐░▌           ▐░▌ ▐░▌      ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌      ▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌            ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌      ▄ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌
 ▀         ▀  ▀         ▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀               ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀ 

""")

# korttipakka
deck_of_cards = [
    "ACE", "ACE", "ACE", "ACE",
    "J", "Q", "K", "J",
    "Q", "K", "J", "Q",
    "K", "J", "Q", "K",
    "2", "2", "2", "2",
    "3", "3", "3", "3",
    "4", "4", "4", "4",
    "5", "5", "5", "5",
    "6", "6", "6", "6",
    "7", "7", "7", "7",
    "8", "8", "8", "8",
    "9", "9", "9", "9",
    "10", "10", "10", "10"
]

# Pelaajan alku rahat
player_money = 1000


def get_cards(cards):
    monikko = ""
    for i in range(0, len(cards)):
        if i < len(cards) - 1:
            monikko += f"{cards[i]}, "
        else:
            monikko += cards[i]
    return monikko


# Palauttaa kortin korttipakalta
# Lisätään otettu kortti pelaajan/diilerin korttipakan ja lisätään pisteitä
def get_a_card(card_index, who):
    card = deck_of_cards[card_index]
    who.append(card)
    if card == "K" or card == "Q" or card == "J":
        return 10
    elif card == "ACE":
        return 1
    else:
        return int(card)


def ask_bet():  # Kysytään pelaajalta panos
    choice = input("Place your bet!!!\n")
    # Alle käsitellään että käyttäjä vain pysty syöttämään numero ei mitään muuta
    if choice.isdigit() or choice[1:].isdigit():
        if int(choice) <= 0:
            print("A bet cant be 0 or lower than zero")
            ask_bet()  # Toistetaan funktio uudelleen
        else:
            choice = int(choice)
            return choice
    else:
        print("A bet can be only a number!!!")
        ask_bet()  # Toistetaan funktio uudelleen


# Funktio tulostaa GAME OVER
def gameover():
    return """
              ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
             ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
            ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
            ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
            ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
             ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
              ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
            ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                  ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                 ░                   
            """


######################################################################################################################
# Pää ohjelma
# Jos totta siis peli loppu
game_over = False
while not game_over:  # Peli alkaa tästä
    random.shuffle(deck_of_cards)  # sekoitetaan korttipakan
    dealer = 0  # Diilerin alkupointti
    dealer_cards = []
    player = 0  # Pelaajan alkupointti
    player_cards = []
    bet_money = 0  # Kolikoitan määrä
    print(f"Player money: {player_money}$")  # Tulostetaan pelaajan raha
    bet = ask_bet()
    bet_money += bet  # tallennetaan panos
    player_money -= bet  # minuus pelaajan raha
    card_index = 0
    times = 0  # jos times on 2 se tarkoittaa että  jokaisella(diilerillä ja pelaajalla) ovat 2 korttia. Käytän tämä sen
    # varten että, pelaaja ei saa nähdä diilerin korttien summa toinen kierros alkaen. Eli pelaaja saa nähdä diilerin
    # korttisumman toka kierroksen asti.
    # Todo: Lisätä lisää kommentteja
    # Todo: Optimoida
    while True:
        if card_index > 51:
            card_index = 0

        # Kortti pelaajalle
        player += get_a_card(card_index, player_cards)
        card_index += 1  # seuraava kortti

        # Kortti diilerille
        if len(dealer_cards) < 2:
            dealer += get_a_card(card_index, dealer_cards)
            card_index += 1

        times += 1
        if times >= 2:
            print(f"Player: {get_cards(player_cards)}")
            print(f"Dealer: {dealer_cards[0]}, ?")
            print()
        if player > 21:
            print(f"Player: {get_cards(player_cards)}")
            print(f"Dealer: {get_cards(dealer_cards)}")
            print()
            print(gameover())
            break
        elif times >= 2:
            choice = input("Do you want to open up? Y/N:\n")
            if choice.upper() == "Y":
                while dealer <= 16:
                    dealer += get_a_card(card_index, dealer_cards)
                    card_index += 1
                print(f"Player: {get_cards(player_cards)}")
                print(f"Dealer: {get_cards(dealer_cards)}")
                if dealer > 21:
                    print("You Won!")
                    player_money += bet_money * 2
                    break
                if player > dealer:
                    print("You Won!")
                    player_money += bet_money * 2
                elif player == dealer:
                    print("Nothing won, nothing lost... at least this time")
                    player_money += bet_money
                else:
                    print(gameover())
                bet_money = 0
                times = 0
                break
            elif choice.upper() == "N":
                print("Continue to Play Dealer!")
    choice = input("Do u want to play again? Y/N:\n")
    if choice.upper() == "N":
        print("See ya!")
        print(f"Player money: {player_money}$")
        game_over = True

