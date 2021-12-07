
import time

def defeatvillain():
    print("A dark green orb of light comes closer towards the main character")
    print("The main villain has found you.")
    print("You see two more men behind him.")
    print("To defeat them you must find their weak spots (hint: aim for the top of their bodies)")
    print()
    powerbar = print("Your powers are fully charged")
    successdefeat = input("Would you like to use your powers? Y/N")
    if successdefeat == "Y":
        print("You hit both of the men with your powers and they are out cold.")
        print()
    elif successdefeat == "N":
        print("You must restart.")
        return(exit())
    if successdefeat == "Y":
        print("The main villain is standing before you.")
        print("You get ready to charge the villain.")
        input("Are you ready to use your powers? Y/N")
    elif successdefeat == "Y":
        print("You hit the villain where it hurts he takes a step back.")
        print("You try to use your powers again but a bright light flashes.")
        print()
    healthbar = print("The villain's health is now at 50%")
    time.sleep(10)


defeatvillain()