cd_suits = {"BS": 9824, "WH": 9825, "WD": 9826, "BC": 9827}
for i in cd_suits:
    print(i)

'''
Black Spade   9824
White Heart   9825
White Diamond 9826
Black Club    9827
'''

suit_str = input("Enter shortened suit:> ")

suit_ansi = int(cd_suits[suit_str])
convertToAscii = chr(suit_ansi)

print(f"The picture of {suit_str} is {convertToAscii}.")
