# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

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
    
    else:
        print("Invalid difficulty level. Please choose Easy or Hard.")

guesses = set_difficulty(difficulty)
print("\nYou Selected {} Mode. You Have {} Guesses.".format(difficulty.title(), guesses))

answer = randint(1, 101)
guess = int(input("Guess a number between 1 and 100: "))

def match(guess):
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

result = match(guess)

while result == False:
    if not guesses == 0:
        print("You have {} guesses left.".format(guesses))
        guess = int(input("Guess again: "))
        result = match(guess)

    elif guesses == 0:
        print(f"You have no more guesses left. The number was {answer}")
        print("You Lose!")
        break