name = input ("Type your name: ").title()
print("Welcome,", name + ", to this adventure!")

game_over = False

while not game_over:
    answer = input("You are on a dirt road. It comes to an end, and you can't go left or right. Which way would you like to go? Type left or right: ").lower()
    if answer == "left":
        while True:
            answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()   
            if answer == "walk":
                print("You walked around and safely made it across.")
                break
            elif answer == "swim":
                print("You swam across and were eaten by an alligator. You lose.")
                break
            else:
                print("Please, type a valid option.")
                continue
        break
    elif answer == "right":
        while True:
            answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type 'cross' or 'back': ").lower() 
            if answer == "cross":
                while True:
                    answer = input("You cross the bridge and meet a stranger. Talk to them? (yes/no): ").lower()
                    if answer == "yes":
                        print("You talked to the stranger, and they helped you to get out of the forest. You WIN!.")
                        game_over = True
                        break
                    elif answer == "no":
                        print("You ignored the stranger and wandered in the forest alone. You got lost. Game over.")
                        game_over = True
                        break
                    else:
                        print("Please, type a valid option.")
                        continue
                break
            elif answer == "back":
                print("You returned to the starting point.")
                break
            else:
                print("Please, type a valid option.")
                continue
    else:
        print("Please, type a valid option.")
        continue

print("Thanks for trying!")