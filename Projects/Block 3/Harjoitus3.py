# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
comma = input("start/stop> ")

mf = input("Gender(Male/Female)> ")
gmgl = float(input("Hemoglobin level> "))

while comma not in {"stop"} or mf not in {"stop"}:
    if mf == "Male" or mf == "male":
        if gmgl > 195:
            print("Level too high!")

            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")

        elif 195 >= gmgl >= 134:
            print("Good! Level is normal.")
            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")

        elif gmgl < 134:
            print("Level too low!")
            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")

    elif mf == "Female" or mf == "female":

        if gmgl > 175:
            print("Level too high!")
            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")

        elif 174 >= gmgl >= 117:
            print("Good! Level is normal.")
            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")

        elif gmgl < 117:
            print("Level too low!")
            mf = input("Gender(Male/Female): ")
            gmgl = float(input("Hemoglobin level: "))

            comma = input("start/stop> ")
    else:
        print("Invalid prompt!")
        mf = input("Gender(Male/Female): ")
        gmgl = float(input("Hemoglobin level: "))

else:
    comma = input("start/stop> ")