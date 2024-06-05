# imports
from changeName import change_name
from clear import clear_terminal

def settings_menu(x):
    clear_terminal()
    print("Welcome to the settings menu,", x)
    print("[1] Change name")
    print("[2] Change font")
    print("[3] Exit settings menu")
    choice = input("Make a selection: ")

    match choice:
        case "1":
            print("You chose to change your name")
            new_name = change_name(x)
            return new_name
        case "2":
            print("You chose to change the font")
            return x
        case "3":
            print("Exiting settings menu...")
            return x
        case _:
            print("You did not make a valid selection.")
            settings_menu(x)
