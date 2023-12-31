import random


def run():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100 (inclusive).")
    difficulty_choice = difficulty()

    if difficulty_choice == 'easy':
        print("You have 10 attempts remaining to guess the number.")
        attempts = 10
    else:
        print("You have 5 attempts remaining to guess the number.")
        attempts = 5

    user_guess = -1

    secret_number = number_generator()

    while user_guess != secret_number and attempts > 0:

        user_guess = int(input("Make a guess: "))

        if user_guess > secret_number:
            print("Too high.")
        elif user_guess < secret_number:
            print("Too low.")

        attempts -= 1

        if attempts > 0:
            print(f"Guesses remaining: {attempts}")
        else:
            print("No guesses remaining.")

    if user_guess == secret_number:
        print(f"You got it! The number was {secret_number}.")
    else:
        print(f"You didn't get it. Too bad! The number was {secret_number}.")

    return


def difficulty():
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return user_difficulty


def number_generator():
    number_to_guess = random.randint(1, 100)

    return number_to_guess
