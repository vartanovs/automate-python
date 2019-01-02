# This is a guess a number game

import random

# Greet user and propmt for name
print('Hello. What is your name?')
name = input()

# Select a random number from 1 to 10
low = 1
high = 20
answer = random.randint(low, high)

print(f'Well, {name}, I am thinking of a number between {low} and {high}.')

# Prompt user for a guess
for guessCount in range(1, 7):
  print('Take a guess!')
  try:
    guess = int(input())
  # If user input triggers a ValueError, trigger a loop to force a digit input
  except ValueError:
    while True:
      print(f'Please guess a number (digit) between {low} and {high}!')
      try:
        guess = int(input())
        break
      except:
        pass

  # Check guess against answer
  if guess == answer:
    # This condition is a correct guess! It breaks the loop.
    print(f'Good job, {name}! You guessed my number in {guessCount} guesses!')
    break
  elif guess < answer:
    print('Your guess is too low.')
  elif guess > answer:
    print('Your guess is too high.')

if guess != answer:
  print(f'Nope. The number I was thinking of was {answer}.')
