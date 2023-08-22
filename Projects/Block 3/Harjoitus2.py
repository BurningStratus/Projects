#- LUX on parvekkeellinen hytti yläkannella.
#- A on ikkunallinen hytti autokannen yläpuolella.
#- B on ikkunaton hytti autokannen yläpuolella.
#- C on ikkunaton hytti autokannen alapuolella.

print("Get description of your floor type here.\nAvailable floor types are: LUX, A, B, C.")
floor = input("Enter you floor type: ")

if floor in {"LUX", "Lux"}:
    print("LUX is the best available class of floors.\nBalcony on the highest floor with the beautiful view!")

elif floor == "A":
    print("A class is high floor with windows with a good view.")

elif floor == "B":
    print("B class is for those who want the balance between the price and comfort.\nWindows aren't an option!")
elif floor == "C":
    print("C is the cheapest option to only to get to the destination.\nNo windows, you live with the cars.")
else:
    print("Prompt isn't recognised. Try again.")
