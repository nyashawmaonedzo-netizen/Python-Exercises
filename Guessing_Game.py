print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")
import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = input("Enter your guess: ")
    attempts += 1
    try:
        user_guess = int(user_guess)
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")    
        