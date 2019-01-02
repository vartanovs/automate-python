# This program plays Rock, Paper Scissors with the user.
import random

possible_moves = ['rock', 'paper', 'scissors']

print('...rock...')
print('...paper...')
print('...scissors...')

# Prompt for Mode
while True:
  mode = input('Play vs human or computer: ')
  if mode == 'human':
    opponent = 'Player 2'
    break
  elif mode == 'computer':
    opponent = 'Computer'
    break
  else:
    print('You must select "human" or "computer"')

# Prompt for Rounds
while True:
  try:
    rounds = input('How many rounds (odd number, up to 9) would you like to play? ')
    rounds = int(rounds)
    if rounds < 1:
      print('Please enter a positive number of rounds.')
    elif rounds > 9:
      print('You can play no more than 9 rounds.')
    elif rounds % 2 == 0:
      print('You must play \'best of\' an odd number of rounds.')
    else:
      break
  except:
    print('Please enter a positive number (digit) between 1 and 9.')

# Initialize score
p1_win_count = 0
p2_win_count = 0

while (p1_win_count < (rounds / 2)) and (p2_win_count < (rounds / 2)):
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
    print(f'{opponent}\'s move is ' + p2_move)

  print('SHOOT!')

  # Helper function to tally win count and print winner declaration message
  def declare_winner(winner):
    global p1_win_count
    global p2_win_count
    if winner == 'p1':
      p1_win_count += 1
      print('Player 1 wins this round!')
    elif winner == 'p2':
      print(f'{opponent} wins this round!')
      p2_win_count += 1
    else:
      print(f'Player 1 and {opponent} tie')

  # Game Win/Loss Logic
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

# Tally final score
if p1_win_count > p2_win_count:
  print('Player 1 wins the Tournament!')
else:
  print(f'{opponent} wins the Tournament!')
