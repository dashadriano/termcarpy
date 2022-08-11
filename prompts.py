# Introduction Prompts
def primer():
    return input("Do you want to start? [y/n]: ")

def greeting():
    print("Car Game Started! Welcome to pyCLI Car Game, made by Dash!")

def help():
    print("""
    Commands available:
        Start — Starts your car engine.
        Stop — Stops the car engine.
        Faster — Accelerates your car.
        Slower — Slows down your car.
        Quit — Exit car game.
        Help — View commands.
    """)

def askName():
    return input("""Hi there! What's your name, driver?

    > """)
    
def secondAskName():
    return input("""What's your name, driver?

    > """)

def welcome(driver):
    print(f"Alright! Hop in, "+driver+"!")



# Start/Stop Prompts
def start():
    print("You've just started the car, nice.")

def stop():
    print("Car stopped. Why are you stopping? Had enough fun for the day?")



# Acceleration/Deceleration Prompts
def faster():
    print("Car speeds up a bit.")

def fastest():
    print("Now we're going SUPAAAAA FAST!")

def slower():
    print("Slowing down a bit. Good call.")



# Invalid Command Prompts
def invalid():
    print("""You seem to have typed an invalid command.
To learn more about commands, bring up the list by typing "help".""")

def invalidName():
    print("""Trying to be mysterious, are we? 
Atleast a single character for your name is required, buddy!""")



# Exit Prompts
def quit():
    print("Game shut down.")

def bye():
    print("Thanks for playing!")

# Maximum Acceleration/Deceleration Reached Prompts
def ceil():
    print("Max speed reached. We can't go faster than this!")

def floor():
    print("We're already at the lowest setting.")
    print("Stopping the car is the only way to go slower at this point!")



# Car State Reminder Prompts
def start():
    print('''Car started! Type "help" for commands if needed!''')

def started():
    print("Car is already started!")

def stopped():
    print("Car is already stopped!")



# Requirement Prompts
def firstStartReq():
    print("Name before keys, buddy!")

def stopReq():
    print("It's already at a stop, tell us your name first though!")

def startReq():
    print("Car must be started first!")

def quitReq():
    print("Car must be stopped first before exiting the game.")

def moving():
    print("Car is still moving. Slow down to minimum speed first before stopping.")



# Assurance for Invalid Answers for Input Prompts
def firstQuitReq():
    return input("""You've typed in a command for exiting the game.
Are you sure you want to exit? [y/n]

    > """)

def needHelp():
    return input("""You've typed in a command for help with commands.
Are you sure you want to bring up list of commands? [y/n]

    > """)



# Response Prompt for Invalid Answers
def assurance():
    print("""That's alright, it's just that you seem to have entered a registered command as your name. 
Try a different one. For list of commands: type "help".""")

# Spacing for Prompts
def space():
    print(" ")