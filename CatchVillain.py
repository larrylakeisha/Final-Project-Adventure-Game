
import time

def catchvillain():
    print("Footsteps echo through your ears.")
    print("You spot the culprit running away from the scene and you start to chase after them.")
    print()
    time.sleep(5)
    powerbar = print("Your powers are at 100")
    successdefeat = input("Would you like to defeat the suspect Y/N")
    if powerbar == 100:
        print("Your powers are fully charged.")
        print("You catch up to the suspect and a powerful blast rushes from your hands.")
        print()
    elif successdefeat == "Y":
        print("The villain is knocked unconscious")
        print("You have successfully caught the villain")
    else:
        return(exit())

    if successdefeat == "Y":
        time.sleep(5)
        print("The suspect awakes.")
        print("You ask the suspect why did they do this and the suspect says their boss made them.")
        print("The suspect gives you the boss's name and their location.")
        print("You try to ask another question but the police show up.")
        print()
        time.sleep(10)



catchvillain()
