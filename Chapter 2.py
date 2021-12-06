import globalvariables
import time

def park():

    print("Chapter 2 begins")
    print("A loud blast shakes the ground, smoke, and flames can be seen from the distance.")
    print("You need to find out who did this")
    print("Pick between these options:")
    choice = 0
    chosenpath = "0"
    while chosenpath == "0":
        print("1. Speak with injured citizens to find out what happened")
        print("2. Speak with the authorities ")
        print("3. Find evidence")
    choice = input("Please pick a path.")
    if choice == "1":
        print("You walk up to a civillian and ask them about the blast.")
        print("They tell you that they seen someone with a black hoodie.")
        print()
        time.sleep(5)
        chosenpath = 1
    elif choice == "2":
        print("You walk over to the police and tell them about the mysterious hooded person.")
        print("The police tell you they will keep an eye out.")
        print("You think to yourself and you decide you will find the person on your own")
        print()
    elif choice == "3":
        print("You decide to look for evidence that may have been left.")
        print("You see footprints that head toward the alley.")
        print("You follow them.")
        print()
        chosenpath = 1
        CatchVillain.catchvillain()


