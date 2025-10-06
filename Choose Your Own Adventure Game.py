"""
Adventure Game
A simple text-based adventure game where the player makes choices to navigate and survive.
Concepts: nested if-else, user input, string methods

"""

print("🏞️ Welcome to the Adventure Game!")

name = input("Type your name: ")
print(f"\n👋 Welcome {name} to the adventure!\n")

answer = input("You are on a dirt road. It comes to an end. Do you want to go left or right? ").lower()

if answer == 'left':
    answer = input("\nYou come to a river. Do you want to 'walk' around it or 'swim' across? ").lower()

    if answer == 'swim':
        print("\n💀 You swam across and were eaten by an alligator. Game Over!")
    elif answer == 'walk':
        print("\n🥵 You walked for miles, ran out of water, and lost the game.")
    else:
        print("\n⚠️ Not a valid option. You lose.")

elif answer == 'right':
    answer = input("\nYou come to a bridge. It looks wobbly. Do you 'cross' or go 'back'? ").lower()

    if answer == 'back':
        print("\n👣 You go back and lose. Game Over!")
    elif answer == 'cross':
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

        if answer == 'yes':
            print("\n💰 The stranger gives you gold. You WIN!")
        elif answer == 'no':
            print("\n😡 You ignore the stranger, they are offended, and you lose. Game Over!")
        else:
            print("\n⚠️ Not a valid option. You lose.")
    else:
        print("\n⚠️ Not a valid option. You lose.")

else:
    print("\n⚠️ Not a valid option. You lose.")

print(f"\n🙏 Thank you for playing, {name}!")
