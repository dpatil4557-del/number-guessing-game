import random

# Computer generates random number
number = random.randint(1, 100)

attempts = 0

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while True:          # loop start
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("🎉 Correct Guess!")
        print("You guessed the number in", attempts, "attempts")
        break         # 👉 LOOP BREAKS HERE (game ends)

    elif guess > number:
        print("Too high! Try again")

    else:
        print("Too low! Try again")