import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Initialize the guess and attempts
attempts = 0
guess = 0

# Start the guessing game
while guess != target_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")