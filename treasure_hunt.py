print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("DO YOU HAVE WHAT IT TAKES?")
print("You haven been given an opportunity to participate in this mysterious game where "
      "unimaginable fortunes and misfortunes await.")
confirmation = input("Do you wish to venture? Y/N\n").upper()

if confirmation == "Y":
    print("Welcome to the game...Remember, every choice matters...ThErE's nO tUrNiNg BaCk NoW...")
    gift_1 = input("You've arrived at the prepare room. There are three boxes box on the table. "
                   "Which color do you want? BLUE/RED/GREEN\n").upper()
    if gift_1 == "BLUE":
        print("You have chosen an empty bottle. May it serve you well :)")
    elif gift_1 == "RED":
        print("You have chosen an edgeless knife. May it serve you well :)")
    elif gift_1 == "GREEN":
        print("You have chosen a pouch of some unknown seeds. May it serve you well :)")
    else:
        print("How unusual.")
    two_doors = input("As you exit the prepare room, you're left with a BLUE and RED door. Which do take?\n").upper()
    if two_doors == "BLUE" and gift_1 == "BLUE":
        print("A typical choice. We'll see.")
    elif two_doors == "RED" and gift_1 == "RED":
        print("A typical choice. We'll see.")
    elif (two_doors == "RED" or two_doors == "BLUE") and gift_1 == "GREEN":
        print("The pouch of seeds moves slightly, but nothing happens.")
    else:
        print("An interesting choice...")
    left_right = input("You exit the door and in front of you is a crossroad. LEFT or RIGHT?\n").upper()
    if left_right == "LEFT":
        a_lake = input("You arrive at a lake. There is a house not too far in the middle of the lake. "
                       "The water is so clear you can see the bottom of it. Do you want to SWIM or WAIT?\n").upper()
        if a_lake == "WAIT":
            island = input("After waiting for a while, in a blink of an you are teleported to the island in the "
                           "middle of the lake. There are three boxes on the ground BLUE, RED, GREEN. "
                           "Your choice?").upper()
            if island == "BLUE" and gift_1 == "GREEN":
                print("The pouch in your pocket reacts with the artifact inside the BLUE box. It grows rapidly! "
                      "Climb the tree and see where it takes you. Your fortune awaits! You win!")
            elif island == "RED" and gift_1 == "GREEN":
                print("The artifact in the box reacts with the pouch in your pocket and burn you to death. "
                      "Thank you for playing!")
            elif island == "GREEN" and gift_1 == "GREEN":
                print("The artifact in the box turns into a hostile walking tree. It wants to consume the "
                      "pouch of seeds in your pocket, and...you too. "
                      "Thank you for playing!")
            elif island == "GREEN" and gift_1 == "RED":
                print("The artifact in the box turns into a hostile walking tree. However, it's trembling by the "
                      "red knife in your hands. It offers to let you see the future at any given time in "
                      "exchange for its life. You win!")
            else:
                print("You got crushed by a meteor. What are the odds huh? Thanks for playing!")
        else:
            print("You have been eaten by an invisible fish. Should have waited. Thank you for playing!")
    else:
        print("You have opened the door to hell. You have been eaten by hell dogs. Thank you for playing!")
else:
    print("You know where to find me :)")