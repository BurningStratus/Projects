dull_value_tobe_deleted = None

# seuraavalla rivilla luku alussa on quest_id, ja sitten 'virallinen nimi'(virallinen nimi != nimi questin alussa)
# 1. STARTER QUEST
def starter_quest_caller():
    print('''
// "Rich" people problems, Monaco

Since you will be away for a while after receiving the message from the debt collectors, 
it might be a bright idea to tell everything your love interest.
    ''')
    user_input_inner = input("Would you like to make a call? Y/N: ")

    if user_input_inner.upper() == "Y":
        dull_value_tobe_deleted = None  ##  here will be money + 50
        print('''
\nAfter a long talk they are quite 'displeased' with the situation. They write you a check for 50$ though.
You go to the nearest bank and receive 50$ with a note:
    "I hope ... debt will teach you. Still love you, ...".
Some parts of the note are incomprehensible because of the water stains on the paper. 
It's time to hit the sky. 
            ''')
    else:
        print('''
You decide that the trip won't be long enough to bother them and depart for good.
It's time to hit the sky.
        ''')

    quest_dict[1] = "DONE"
    return 0
    # END OF STARTER QUEST


# 2. CHESS IN GERMANY
def chess_in_germany_caller():
    print('''
"Chess maybe?", Germany

While walking through the park in Germany, you see an old man sitting on a bench with a smoking pipe and a chess board, 
with all pieces being set up for a new game. The old man asks you to play with him. 
At school you loved to play chess.
    ''')
    user_input_inner = input("Do you want to challenge him? Y/N: ")
    if user_input_inner.upper() == "Y":
        print('''
After a long and exhausting game you take a victory from the old man. He is very pleased with a game
and after you tell them about your problem, he tells you about leprechauns in Ireland, that give out gold for some reason.
"What a weirdo" - Was your first thought.
        ''')
    else:
        print('''
You choose to ignore the old man, because you don't have time for stupid games.
        ''')

    quest_dict[2] = "DONE"
    return 0
    # END OF CHESS IN GERMANY


# 3. POLISH INCIDENT
def polish_incident_caller():
    dull_value_tobe_deleted = None  # here will be money - 100
    print('''
\n//Live and let live, Poland

When landing on the lane, one of your tyres pops. You land the plane no problem, since you are an experienced pilot.
Too bad that the spare tyre has been in the trunk for long enough for it rot through. 
You spend the entire day trying to navigate the city and find the tyre with the right size. 
You spend 100$ on it. 
Returning to the airport, where you plane is parked, you feel exhausted.
    ''')
    user_input_inner = input("Do you want to pay airport mechanic 200$ for him to change your tyre? Y/N: ")

    if user_input_inner.upper() == "Y":
        dull_value_tobe_deleted = None  # here will be money -200
        print('''
You go to the mechanic's hangar and ask him to swap a rotten tyre for a new one. 
He swiftly puts a new tyre on an old rim with seems like no effort, but with enthusiasm. 
You spend the remaining day walking around the city and looking at lots of poor people selling lots of things.
        ''')
    elif user_input_inner.upper() == "N":
        print('''
You sit through the whole evening until the night trying to change a tyre. Not a pleasant activity.
When you are finally done with the tyre, you bring the borrowed tools back to the repair hangar. 
There you spot an airport mechanic filling gas cans with kerosene. This certainly wasn't an authorized activity.
        ''')
        user_input_inner = input("He didn't notice you. Do you want to confront him? Y/N: ")

        if user_input_inner.upper() == "Y":
            print('''
When you come closer to the mechanic, he finally sees you and looks pissed. 
Since you see him engaging in not-so-legal activities, 
he tells you that he will give 100$ and 300 L of aviation fuel(1x FREE TRAVEL)
If you won't tell anyone.
            ''')
            user_input_inner = input("Contact the mechanic's superiors? Y/N: ")

            if user_input_inner.upper() == "N":
                dull_value_tobe_deleted = None  # here will be money +100
                dull_value_tobe_deleted = None  # price of travel = '0' for 1 move
                print('''
You decide to not to interrupt the direction of the universe, 
so you accept 300 L and 100$ of kerosene and leave with peace.
                ''')
            else:
                dull_value_tobe_deleted = None  # here will be money -100
                print('''
You decide that the world will be better if you tell the airport security that the mechanic is stealing the kerosene.
When you tell the patrolling guard about it, he tells you that they will 'deal' with the mechanic. 
Feeling great after doing the right thing, you go back to your motel. 
In the morning you notice that another tyre is punctured. 
Strange to see this, because it was brand-new: you changed it the day before the 'message'.
So you spend another 100$ to change it, and depart peacefully the next day.
                ''')
        else:
            print('''
You decide not to interrupt him from their daily activities, 
so you bring the tools back on their places and peacefully leave the hangar. 
Then you go back to the motel and depart the next day. 
            ''')
    quest_dict[3] = "DONE"
    return 0

# 4. BLACK CAT

