# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from art import logo
from random import randint

print(logo)
print("\nWelcome to Guess The Number Game!")
print("\nI have a number between 1 and 100. Can you guess it?")

difficulty = input("Choose a Difficulty Level 'Easy' or 'Hard': ").lower()

def set_difficulty(difficulty):
    """Set the difficulty level"""
    if difficulty == "easy":
        return 10
    
    elif difficulty == "hard":
        return 5

guesses = set_difficulty(difficulty)
print("\nYou Selected {} Mode. You Have {} Guesses.".format(difficulty.title(), guesses))

answer = randint(1, 101)
guess = int(input("Guess a number between 1 and 100: "))

def match(guess, answer):
    """Check if the guess is correct or not"""
    global guesses
    if guess == answer:
        print(f"You guessed it! The answer was {answer}")
        print("You Win!")
        return True
    
    else:
        if guess > answer:
            print("Too High!")
            guesses -= 1
            return False       
        
        elif guess < answer:
            print("Too Low!")
            guesses -= 1
            return False

result = match(guess, answer)

while result == False:
    if not guesses == 0:
        print("You have {} guesses left.".format(guesses))
        guess = int(input("Guess again: "))
        result = match(guess, answer)

    elif guesses == 0:
        print(f"You have no more guesses left. The number was {answer}")
        print("You Lose!")