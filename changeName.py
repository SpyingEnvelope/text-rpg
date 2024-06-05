from clear import clear_terminal

def change_name(name):
    clear_terminal()
    new_name = input("Please enter the new name:")
    print("Old name: ", name)
    print("New name: ", new_name)
    return new_name
