import random

print("🎯 Welcome to the Number Guessing Game!")

top_of_range = input("Enter the maximum number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("⚠️ Please type a number greater than 0 next time.")
        quit()
else:
    print("⚠️ Please type a valid number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("⚠️ Please enter a valid number.")
        continue

    if user_guess == random_number:
        print(f"🎉 You got it! The number was {random_number}.")
        break
    elif user_guess > random_number:
        print("⬆️ Too high! Try again.")
    else:
        print("⬇️ Too low! Try again.")

print(f"🏆 You got it in {guesses} guesses!")
