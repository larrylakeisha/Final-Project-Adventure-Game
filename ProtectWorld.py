import globalvariables
import time

def protectworld():
    print("The villain falls to the ground and the earth shakes.")
    print("You get ready to finish this you begin to charge your powers.")
    powerbar = print("Your powers are now at 100% Do you want to use them? Y/N")
    if globalvariables.successdefeat == "Y":
        print("You use all of the force you have and let out a cry.")
    healthbar = print("The villain's health is now a 25%")
    print("You being to speak with the villain you ask him why does he want to end the world")
    print("The villain laughs and tells you if you defeat him more is to come")
    defeatvillain = print("Would you like to speak with the villain more or defeat him? Pick 1 or 2")
    if defeatvillain == "1":
        print("You ask the villain more about where your powers come from he tells you that are a descendant from an alien planet on jupiter.")
        print("Before you can ask more questions the villain is knocked unconscious.")
        print("You have successfully defeated the villain.")
        print()
    if defeatvillain == "2":
        print("You waste no time defeating the villain you use the rest of your built up power to defeat him.")
        print("You sigh a breath of relief and collapse on the ground.")
        print("You have successfully defeat the villain.")
        print()
        time.sleep(10)
        globalvariables.success = True
        return()


