print('Welcome to my computer quiz!')

playing = input('Do you want to play?(yes/no) ')

if playing.lower() != 'yes':
    print("Maybe next time! 👋")
    quit()

print("Okay! Let's play 😀")
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('✅ Correct!')
    score+=1
else:
    print("❌ Incorrect!")

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect!")

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect!")

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('✅ Correct!')
    score += 1
else:
    print("❌ Incorrect!")

print("\n--- Results ---")
print(f"🎯 You got: {score} out of 4 correct!")
print(f"📊 Your score: {(score/4)*100:.2f}%")

if score == 4:
    print("🏆 Excellent! Perfect score!")
elif score >= 2:
    print("👍 Good job! Keep practicing.")
else:
    print("📚 Keep learning, you’ll get better!")

