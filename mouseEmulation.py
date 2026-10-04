import mouse 
import keyboard

menudict = {
    "left": "a",
    "right": "d",
    "up": "w",
    "down": "s",
    "leftClick": "q",
    "rightClick": "e",
    }

def printMenu():
    print("Press [c] to configure mapping")
    print("Press [p] to print mapping")
    print("Press [s] to start mapping")
    print("Press [ESC] to quit application")


def usersConfig():
    print("Please enter the keys for the following mouse movements:")
    menudict["left"] = input("Enter the key for moving left: ")
    menudict["right"] = input("Enter the key for moving right: ")
    menudict["up"] = input("Enter the key for moving up: ")
    menudict["down"] = input("Enter the key for moving down: ")
    menudict["leftClick"] = input("Enter the key for left click: ")
    menudict["rightClick"] = input("Enter the key for right click: ")

def printMapping():
    print("Current mapping:")
    for action, key in menudict.items():
        print(f"{action}: {key}")

def startMapping():
    print("Starting mouse emulation. Press [ESC] to stop.")
    while True:
        if keyboard.is_pressed(menudict["left"]):
            mouse.move(-50, 0, absolute=False, duration=0.2)
        elif keyboard.is_pressed(menudict["right"]):
            mouse.move(50, 0, absolute=False, duration=0.2)
        elif keyboard.is_pressed(menudict["up"]):
            mouse.move(0, -50, absolute=False, duration=0.2)
        elif keyboard.is_pressed(menudict["down"]):
            mouse.move(0, 50, absolute=False, duration=0.2)
        elif keyboard.is_pressed(menudict["leftClick"]):
            mouse.click(button='left')
        elif keyboard.is_pressed(menudict["rightClick"]):
            mouse.click(button='right')
        elif keyboard.is_pressed("esc"):
            print("Mouse emulation stopped.")
            break

def runMouseEmulationApplication():
    while True:
        printMenu()
        user_choice = input("Enter your choice and press Enter: ")

        if user_choice == "esc":
            print("Application closed.")
            exit(0)
        elif user_choice == "c":
            usersConfig()
        elif user_choice == "p":
            printMapping()
        elif user_choice == "s":
            startMapping()
        else:
            print("Invalid choice. Please try again.")