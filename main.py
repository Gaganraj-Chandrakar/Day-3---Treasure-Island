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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are in your way to make your first decision.\nYou have two ways in front of you.\nLeft one says lie and "
      "right one says lie.\nLeft says It is true that I don't have treasure.\nRight says I speak truth and It is "
      "false that it is true that I don't have treasure.")
first_choice = input("Which way will you choose? Left/Right: ")
if first_choice.lower() == "left":
    print("You have chosen the right way.")
    second_choice = input("Which way will you choose? Wait/Swim: ")
    if second_choice.lower() == "wait":
        print(
            "A sailor came on boat and you climb on boat to get to the other. Well guess what he was a theif carrying "
            "lots of gold in his boat. You were killed by the sailor. Game Over")
    elif second_choice.lower() == "swim":
        print(
            "You were eaten by the bird swimming in the river. Game Over...\nBut wait birds aren't real. So you "
            "survived"
            "and crossed the river.\nYou were hungry so you ate some crocodile on the way.")
        print(
            "You are on the way to your last decision. Choose wisely.\nYou go inside a castle. You are just a door away"
            "from the treasure.\nThere are 3 doors infront of you. A red door, a yellow door, and a blue door.")
        third_choice = input("Which door do you choose? Red/Yellow/Blue: ")
        if third_choice.lower() == "red":
            print("You are burned by fire. Obvious, isn't it? Red = Fire. Game Over")
        elif third_choice.lower() == "yellow":
            print("You found the treasure. Well Done. You died. Don't ask how. Game Over")
        elif third_choice.lower() == "blue":
            print(
                "You found the Treasure Well Done!\nYou opened the box and you found lots of gold coins and a note on "
                "paper.\nIt says The person who chose Yellow door got the box with bomb. Wish him luck.")
elif first_choice.lower() == "right":
    print("You have chosen the wrong way. You are eaten by a hot girl. But why are you happy? Anyways, GAME OVER.")
