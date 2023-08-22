#talent = 20 pounds
#pound = 32 lots
#lot = 13.3 g

# We need to convert them to kilos and grams.

talent_r = input("Talents: ")
pound_r = input("Pounds: ")
lot_r = input("Lots: ")

talnt = float(talent_r)
pnd = float(pound_r)
lot = float(lot_r)

#converting all currencies down to grams, and then sum them all
conv_talnt = talnt * 20 * 32 * 13.3
conv_pnd = pnd * 32 * 13.3
conv_lot = lot * 13.3

summ_g = conv_lot + conv_talnt + conv_pnd

kilos = summ_g/1000
grams = (kilos % 1) * 1000


print( f"Kilograms: {kilos:6.0f}" + f" Grams:  {grams:6.0f}")
