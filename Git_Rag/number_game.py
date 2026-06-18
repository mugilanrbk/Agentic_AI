"""
number_game.py
An interactive guessing game using loops and error handling.
"""
import random

def start_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            # Prompt user and safely convert input to integer
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found the number in {attempts} attempts.")
                break # Exit loop
                
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

if __name__ == "__main__":
    start_game()
