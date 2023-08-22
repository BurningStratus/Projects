# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

mf = input("Gender(Male/Female): ")
gmgl = float(input("Hemoglobin level: "))

if mf == "Male":
    if gmgl > 195:
        print("Level too high!")
    elif 195 >= gmgl >= 134:
        print("Good! Level is normal.")
    elif gmgl < 134:
        print("Level too low!")
elif mf == "Female":
    if gmgl > 175:
        print("Level too high!")
    elif 174 >= gmgl >= 117:
        print("Good! Level is normal.")
    elif gmgl < 117:
        print("Level too low!")