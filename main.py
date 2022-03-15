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

difficulty = input("Choose A Difficulty Level 'Easy' or 'Hard': ").lower()

def set_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid difficulty level. Please choose Easy or Hard.")

guesses = set_difficulty(difficulty)
print("\nYou Selected {} Mode. You Have {} Guesses.".format(difficulty.title(), guesses))

answer = randint(1, 101)
print("Answer is", answer)

guess = input("Guess A Number: ")

def match(guess):
    if guess == answer:
        print("You Win!")
        return True
    
    else:
        if guess > answer:
            print("Too High!")
            return False
        
        elif guess < answer:
            print("Too Low!")
            return False