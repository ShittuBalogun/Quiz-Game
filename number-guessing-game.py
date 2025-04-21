import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries ")
        except ValueError:
            print("Please enter a valid number.\n")

# Run the game
guessing_game()
