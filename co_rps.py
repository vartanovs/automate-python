# This program plays Rock, Paper Scissors with the user.
import random

possible_moves = ['rock', 'paper', 'scissors']

print('...rock...')
print('...paper...')
print('...scissors...')

# Prompt for Mode
while True:
  mode = input('Play vs human or computer: ')
  if mode in ['human', 'computer']:
    break
  else:
    print('You must select "human" or "computer"')

# Prompt Player 1
while True:
  p1_move = input('(Enter Player 1\'s choice): ')
  if p1_move in possible_moves:
    break
  else:
    print('You must select "rock", "paper" or "scissors"')

# Prompt Player 2 (if mode is human) ...
while mode == 'human':
  p2_move = input('(Enter Player 2\'s choice): ')
  if p2_move in possible_moves:
    break
  else:
    print('You must select "rock", "paper" or "scissors"')

# ... or auto-generate Player 2's move (if mode is computer)
if mode == 'computer':
  p2_move_index = random.randint(0,2)
  p2_move = possible_moves[p2_move_index]
  print('Player 2\'s move is ' + p2_move)

print('SHOOT!')

# Helper function to print winner declaration message
def declare_winner(winner):
  if winner == 'p1':
    print('Player 1 wins!')
  elif winner == 'p2':
    print('Player 2 wins!')
  else:
    print('Player 1 and Player 2 tie')

# Game Logic
if p1_move == p2_move:
  declare_winner('tie')
elif p1_move == 'rock':
  if p2_move == 'scissors':
    declare_winner('p1')
  else:
    declare_winner('p2')
elif p1_move == 'paper':
  if p2_move == 'rock':
    declare_winner('p1')
  else:
    declare_winner('p2')
else:
  if p2_move == 'paper':
    declare_winner('p1')
  else:
    declare_winner('p2')
