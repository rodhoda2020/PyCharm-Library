# Program which the user chooses their own story.

print("\nYou are walking down a trail that divides into two paths.")
choice_1 = input("Do you go left or right?\n")


def main_story():
    input("You have chosen to go left. Press enter to continue.")
    print("\nYou come across a wild lion!")
    print("You do not have anything to fight the lion. You can either try to hide or run away.")
    choice_2 = input("What do you do?\n")
    if choice_2 == "run away":
        print("Unfortunately, the lion was too fast. You have been killed.")
    if choice_2 == "hide":
        input("Luckily, the lion didn't see you yet and you were able to hide. Press enter to continue.")
        print("\nYou patiently wait until the lion goes away so that you can safely continue your journey.\n")
        choice_5 = input("You continue going down the path and eventually stumble upon a sword. Will you 'pick up' or "
                         "'leave it'?")
        if choice_5 == "pick up":
            print("\nYou have decided to pick up the sword.\n")
if choice_1 == "left":
    main_story()
if choice_1 == "right":
    input("You have chosen to go right. Please enter to continue.")
    print("You reach a dead end")
    choice_3 = input("Type 'go back' to go back to the main trail\n")
    if choice_3 == "go back":
        choice_4 = input("You have now gotten back to the main trail. Do you wish to go left this time?\n")
        if choice_4 == "yes":
            main_story()
        else:
            exit()

input("\n\nPress enter to exit.")