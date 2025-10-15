print('''.______________________________________________________________________________.
|       _    _         _    _        _    _         _    _        _    _       |
|  /}    \/}/     /}    \/}/     /}   \/}/     /}    \/}/     /}   \/}/     /} |
|_/|\_    |_    _/|\_    |_    _/|\_   |_    _/|\_    |_    _/|\_   |_    _/|\_|
| / \     | \    / \     | \    / \    | \    / \     | \    / \    | \    / \ |
|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|
|                                                                              |
|                         Welcome to The Treasure Island                          |
|                                                                              |
|     _                                                                  _     |
|    /_\                                                                /_\    |
|    =|=                                                                =|=    |
|               .*.                                          .*.               |
|              ;(;);________________________________________;(;);              |
|              |;;;    _    _         _    _        _    _   ;;;|              |
|              | ;/}    \/}/     /}    \/}/     /}   \/}/    /; |              |
|              |_/|\_    |_    _/|\_    |_    _/|\_   |_   _/|\_|              |
|              | / \     | \    / \     | \    / \    | \   / \ |              |
|            __|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|__            |
|___________|______________________________________________________|__________lc
  
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the  Exit door .")
choice1= input('you\' are  at a crossroad , where do you want to go ? '
'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake.'
        'There is an island in the middle of the lake.'
        'Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        "There is a house with 3 doors. One red, "
                        "one yellow and blue."
                        "Wich colour do you choose?\n").lower()
        if choice3 =="red":
            print("It's a room full of fire. Game Over")
        elif choice3 =="yellow":
            print("You found the treasure. You Win!")

        elif choice3 == "blue":
             print("You enter a room of beast. Game Over")
        else:
            print("You chose a door that doesn`t exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")


if choice1 == "right":
    choice2 = input('You\'ve come to a Pirate Ship.'
                    'There is a Zombie  on board .'
                    'Type "fight" to kill the a zombie. '
                    'Type "run" to  run away  .\n').lower()
    if choice2 == "fight":

        choice3 = input("You got  got on board  unarmed."
                        "There is a coff  with 3 weapons. One hammer, "
                        "one sword and rifle."
                        "Wich weapon do you choose?\n").lower()
        if choice3 == "sword":
            print("Zombie overpowered your sword swing . Game Over")
        elif choice3 == "hammer":
            print(" You got Beaten by the zombie  . Game  Over!")

        elif choice3 == "rifle":
            print("HEADSHOT . YOU WIN")

else:
 print("You fell in to  a hole . Game Over")
