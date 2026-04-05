# ===============================================================
# Number Guessing Game
# ===============================================================

# 1. Import random
import random

# ---------------------------------------------------------------

# 2. Generate random number
number = random.randint(1, 100)

# ---------------------------------------------------------------

# 3. Ask user input
guess = int(input("Enter your guess: "))

# ---------------------------------------------------------------

# 4. Repeat until correct
while guess != number:
    # Compare guess & Give hint (high/low)
    if guess > number:
        print("Too high! Number is lower.")
    else:
        print("Too low! Number is higher.")

    guess = int(input("Enter your guess: "))

# ---------------------------------------------------------------

# 5. Success message
print(f"Congratulations! You guessed the correct number -> {number}")

# ---------------------------------------------------------------