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

    user_guess = int(input("Make a guess: "))

    number_generator(user_guess)


def difficulty():
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return user_difficulty


def number_generator(user_guess):
    number_to_guess = random.randint(1, 100)

    if user_guess > number_to_guess:
        print("Too high.")
    elif user_guess < number_to_guess:
        print("Too low.")
