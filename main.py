import random
import time
import sys

gold = 0

friendlyDragon = r"""
      /\_/\\
     ( o.o )
      > ^ <
"""

fireDragon = r"""
      /\__/\
     ( 🔥🔥 )
      >^^^<
"""

iceDragon = r"""
      /\__/\
     ( ❄️❄️ )
      >^^^<
"""

goldenDragon = r"""
      /\__/\
     ( 👑👑 )
      >^^^<
"""

# display an introduction
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
    print("In front of you, you see 4 caves")
    print("In one cave, the dragon is friendly and will share treasure with you")
    print("The other dragons are hungry and will eat you on sight")
    print()


def chooseCave():
    cave = input('Cave 1 or 2 or 3 or 4: ')

    if cave not in '1234':
        print("Error")
        sys.exit(0)

    return int(cave)


def checkCave(chosenCave):
    global gold

    print('\nYour heart races as you approach the dragon cave...')
    time.sleep(2)

    print('The air grows cold and silent...')
    time.sleep(2)

    print('A large dragon jumps out in front of you!')
    time.sleep(2)

    print('It opens its jaws and...\n')
    time.sleep(2)

    dragonType = random.choice([
        "Friendly Dragon",
        "Fire Dragon",
        "Ice Dragon",
        "Golden Dragon"
    ])

    if dragonType == "Friendly Dragon":
        print(friendlyDragon)
        print("🐉 Friendly Dragon")
        print("Greets you before sharing treasure!")
        gold += 50

    elif dragonType == "Fire Dragon":
        print(fireDragon)
        print("🔥 Fire Dragon")
        print("Breathes fire and scares you away!")
        gold -= 25

    elif dragonType == "Ice Dragon":
        print(iceDragon)
        print("❄️ Ice Dragon")
        print("Freezes the cave entrance!")

    elif dragonType == "Golden Dragon":
        print(goldenDragon)
        print("👑 Golden Dragon")
        print("Shares a chest full of gold!")
        gold += 100

    print("\n💰 Gold:", gold)

    # WIN CONDITION
    if gold >= 200:
        print("\n🏆 CONGRATULATIONS! 🏆")
        print("You collected 200 gold and became the Dragon King!")
        sys.exit()

    # LOSE CONDITION
    if gold < 0:
        print("\n💀 GAME OVER 💀")
        print("You ran out of gold!")
        sys.exit()


# Main program
while True:
    displayIntro()

    caveNumber = chooseCave()
    checkCave(caveNumber)

    playAgain = input("\nDo you want to play again? (yes or no): ").lower()

    if playAgain == "yes":
        print("\nStarting a new adventure...")
        time.sleep(2)

    elif playAgain == "no":
        print("\nGame ended")
        break

    else:
        print("\nInvalid input")
        break

print("Thanks for playing! 🐉")
