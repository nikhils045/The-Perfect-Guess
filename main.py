import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the target number (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the right number in {attempts} attempts.")
            break
        elif guess > target_number:
            print("Too High! Try again.")
        else:
            print("Too Low! Try again.")
    
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again == "y":
            play_game()
            break
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

play_game()