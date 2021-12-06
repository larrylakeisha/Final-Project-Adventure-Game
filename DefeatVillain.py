import globalvariables
import time

def defeatvillain():
    print("A dark green orb of light comes closer towards the main character")
    print("The main villain has found you.")
    print("You see two more men behind him.")
    print("To defeat them you must find their weak spots (hint: aim for the top of their bodies)")
    print()

    if globalvariables.powerbar == 100:
        print("Your powers are fully charged")
        successdefeat = input("Would you like to use your powers? Y/N")
    if globalvariables.successdefeat == "Y":
        print("You hit both of the men with your powers and they are out cold.")
        print()
    elif globalvariables.successdefeat == "N":
        print("You must restart.")
        return(exit())
    if globalvariables.successdefeat == "Y":
        print("The main villain is standing before you.")
        print("You get ready to charge the villain.")
        print("Are you ready to use your powers? Y/N")
    elif globalvariables.successdefeat == "Y":
        print("You hit the villain where it hurts he takes a step back.")
        print("You try to use your powers again but a bright light flashes.")
        print()
    healthbar = print("The villain's health is now at 50%")
    time.sleep(10)
    ProtectWorld.protectworld()
