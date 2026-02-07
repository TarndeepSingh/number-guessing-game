from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(guess, answer):
    """Compare the user's guess with the actual answer."""
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"🎉 You got it! The answer was {answer}.")
        return True


def set_difficulty():
    """Ask the user to choose a difficulty level."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("❌ Invalid choice. Please type 'easy' or 'hard'.")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        is_correct = check_guess(guess, answer)

        if is_correct:
            return

        turns -= 1

        if turns == 0:
            print(f"\n💀 You've run out of guesses. The number was {answer}.")
        else:
            print("Guess again.")


# Start game
play_game()
