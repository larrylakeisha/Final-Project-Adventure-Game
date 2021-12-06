# Lakeisha Larry
# November 15, 2021

# Global variable contains variables and updated them as the game continues.

def globalVariables():
    # global variable for choices
    global playername
    global powerchoice
    global speakchoice
    global explorechoice
    global objectives
    global usepowers
    global healthbar
    global powerbar
    global villainchoice
    global success
    global restartcheckpoint

    playername = "" # player enters their name
    powerchoice = " " # determines if the player choose to learn powers
    speakchoice = " " # determines if player chose to speak to the hero
    explorechoice = " " # determines if player chose to explore city
    objectives = " " # keeps place of which task the player choose
    healthbar = 0 # decides the health of the villains
    powerbar = 0 # decides if special superpower is ready to be used
    villainchoice = " " # determines if player chooses to speak with the villain or defeat them
    success = " " # checks if player successfully defeats the villain
    restartcheckpoint = " " # restarts the game from checkpoint
