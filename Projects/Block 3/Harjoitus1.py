#kuhan pituus. Jos alle 37cm = alamittainen. Yli = hyv'

lengthstr = input('Fish length(cm): ')

length = float(lengthstr)

if length > 37:
    print(f'Good! {length:2.0f}', "cm fish is big enough.")

elif length <= 37:
    addlght = (37 - length)
    print('Fish is too small!', f'{addlght:2.0f}', ' cm to go.')
