name = input("Type you name ")
print("Welcome", name, "to this adventure!")

quest = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go>").lower()

if quest == "left":
    quest = input("YOu come to a road, you can walk around it or swim across? Type walk to walk around it and swim to swim across it: ")
    if quest == "swim":
        print("YOu swam accross and were eaten by a Crocodile")
    elif quest == "walk":
        print("You walked for many miles, and ran out of energy")
    else:
        print("Not a valid option. YOu lose!!")

elif quest == "right":
    quest = input("You came to a bridge. It looks wobbly, do you wanna cross or head back? (cross/back)")
   
    if quest == "back":
        print("You go back and lose. ")
    elif quest == "cross":
        quest = input("You cross the bridge and meet a stranger, do you talk to them (yes/no)")
      
        if quest == "yes":
            print("You talk to the stranger and you got a gold, and you win")
        elif quest == "no":
            print("You ignore the stranger and they are offended and you lose ")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option, You lose")
else:
    print("Not a valid optionl. You lose.")
print("Thank you for trying this game", name)
