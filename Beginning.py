import globalvariables
import time
import Base



def schoolbuilding():

    choice1 = "0"
    globalvariables.playername = input("Your new powers await you. To begin type your name.")
    startanswer = input("Are you ready to begin? Y/N")
    startgame = 0
    if startanswer == "N":
        print("Aren't you ready to save the world")
        startgame = 0
        return(exit())
    elif startanswer == "Y":
        startgame = 1
        print("The game will now begin")
        startgame = 1
    if startgame == "Y":
        chap1_intro()
        choice1 = "0"
        startgame = False
    if startgame == "Y":
        print("A bright light shines, and a young girl stands in front of a school")
        print()
        print("You are greeted with a tall figure who looks to be a hero")
        print()
        print("The hero tells you must help defeat a powerful villain with your new powers")
        print()
        print("1. Explore the city")
        print("2. Learn more about your powers by speaking with the hero")
        print("3. Learn how to use your powers")
        print()
    choice1 = "0"
    while startgame == False:
            choice1 = input("What would you like to do? 1. explore the city, 2. Speak with the hero, or 3. Learn how to use your powers?")
            if choice1 == "1":
                print("You begin to the park")
                print()
                print("You arrive at the park when you see a commotion")
                print()
            elif choice1 == "2":
                print("The hero tells you that you must learn how to use your powers before you defeat the villain.")
                print()
                print("Try again.")
                print()
            restartcheckpoint = input("Would you like to restart? Y/N")
            if restartcheckpoint == "Y":
                Chapter1.schoolbuilding()
            else:
                return(exit())
            if choice1 == "3":
                print("Your powers come with a special power which will be used to defeat the villain.")
                print()
            if restartcheckpoint == "Y":
                Chapter1.schoolbuilding()
            else:
                return(exit())
            if startmodule2 == True:
                print("A blast shakes the city.")
                print()
            time.sleep(10)
            chapter2.park()