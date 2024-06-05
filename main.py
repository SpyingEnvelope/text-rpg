# import
from settings import settings_menu
from clear import clear_terminal
from game_logo import draw_logo

def name_selection():
    clear_terminal()
    x = input("Please input your character's name: ")
    print("You have selected", x)
    input_function(x)

def input_function(x):
    clear_terminal()
    print("Is", x, "correct? ")
    choice = input("[Y]es or [N]o? ")
    if choice.lower() == "y" or choice.lower() == "yes":
        print("Great! Welcome", x)
        menu_selection(x)
    elif choice.lower() == "n" or choice.lower() == "no":
        print("Well, let's try again!")
        name_selection()
    else:
        print("You did not make a valid choice. The only two valid choice are y and n")
        input_function(x)

def menu_selection(x):
    clear_terminal()
    draw_logo()
    print("Please choose what you want to do, " + x + ": ")
    print("[1] Start New Game")
    print("[2] Load Saved Game")
    print("[3] Settings")
    print("[4] Exit game")

    selected = input("Enter selection: ")

    match selected:
        case "1":
            print("You selected new game")
        case "2":
            print("You selected to load a saved game")
        case "3":
            print("You selected to go into the settings menu")
            name_selection = settings_menu(x)
            menu_selection(name_selection)
        case "4":
            print("Thank you for playing Text Adventure!")
            print("Exiting game...")
            exit()
        case _:
            print("You have made an invalid selection.")
            menu_selection(x)

name_selection()
