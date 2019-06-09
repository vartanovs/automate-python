# This program check's a user's age to determine club entry
age = None
while not age:
  age = input('How old are you: ')

# Cast age to an integer (no error handling for now)
age = int(age)

# Flow control to determine status
if age >= 21:
  print('You are good to enter.')
elif age >= 18:
  print('You can enter, but must wear a wristband.')
else:
  print('You shall not pass.')
