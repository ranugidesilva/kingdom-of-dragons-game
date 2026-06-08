import random
import time
#display an introduction
def displayIntro():
    print(r"""
           / \  //\
      |\___/|      /   \//\\
      /O  O  \__  /    // | \ \
     /     /  \/_/    //  |  \ \
     @_^_@/   \/_   //    |   \ \
     //_^_/     \/_ //    |    \ \
    """)

    print("You are in the KINGDOM OF DRAGONS 🐉")
    print("In front of you, you see 5 caves")
    print("In one cave, the dragon is friendly and will share treasure with you")
    print("The other dragon is hungry and will eat you on sight")
    print()
    
def chooseCave():
    cave = ' '
    cave = input('Cave 1 or 2 or 3 or 4 or 5:')
    if cave not in '12345':
        print("Error")
        sys.exit(0)
        return int(cave)
def checkCave(chosenCave):
    print('\nYou approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you!')
    time.sleep(2)
    print('He opens his jaws and...\n')
    time.sleep(2)

    dragonType = random.choice([
        "Friendly Dragon",
        "Fire Dragon",
        "Ice Dragon",
        "Golden Dragon"
    ])

    if dragonType == "Friendly Dragon":
        print("🐉 Friendly Dragon")
        print("Greets you before sharing treasure!")

    elif dragonType == "Fire Dragon":
        print("🔥 Fire Dragon")
        print("Breathes fire and scares you away!")

    elif dragonType == "Ice Dragon":
        print("❄️ Ice Dragon")
        print("Freezes the cave entrance!")

    elif dragonType == "Golden Dragon":
        print("👑 Golden Dragon")
        print("Shares a chest full of gold!")
    else:
        print('Gobbles you down!\n')
#Main program
displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)

import time
playAgain = input("Do you want to play again? (yes or no): ")

if playAgain == "yes":
    print("Game will restart")
elif playAgain == "no":
    print("Game ended")
else:
    print("Invalid input")
time.sleep(3)
print("Thanks for playing!")
