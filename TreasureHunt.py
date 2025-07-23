print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to The Island. \nYou will be given a bunch of choices and the goal is to find the treasure."
      " Obviously.")
print("Your mission is to find the treasure.")
cr = input("You're at a crossroads, would you like to go left or right?\n")

if cr == "left":
    ls = input("You've found an island in the middle of a lake. Would you like to wait for a boat or swim towards it?\n")
    if ls == "wait":
        door = input("You've arrived at the island unharmed, "
                     "there's a large house with 3 coloured doors, red, blue, and yellow.\n"
                     "Which one would you like to go through?\n")
        if door == "red":
            print("You burned in a room on fire. \nGame Over.")
        elif door == "blue":
            print("A guard dog attacked you. \nGame Over.")
        elif door == "yellow":
            print("Congrats!! You found the treasure!")
        else:
            print("Typo? Try again.")
    elif ls == "swim":
        print("Chose swim. You got eaten by an Alligator. \nGame Over")
    else:
        print("Typo? Try again.")
elif cr == "right":
    print("Chose right. You fell into a hole. \nGame Over.")
else:
    print("Typo? Try again.")
