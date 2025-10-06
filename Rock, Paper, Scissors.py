import random

print("🎮 Welcome to Rock, Paper, Scissors!")

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("⚠️ Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("👩🏼‍🦰 You picked", user_input + ".")
    print("💻 Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("🤝 It's a tie!")

    elif user_input == 'rock' and computer_pick == 'scissors':
        print("✅ You won!")
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print("✅ You won!")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("✅ You won!")
        user_wins += 1

    else:
        print("❌ You lost!")
        computer_wins += 1

print("\n--- Game Over ---")
print("🏆 You won", user_wins, "times.")
print("💻 The computer won", computer_wins, "times.")
print("👋 Thanks for playing!")


