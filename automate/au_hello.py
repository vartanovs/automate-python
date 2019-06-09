# This program greets the user and asks for their name and age

print('Hello World!')

# Ask user for their name
print('What is your name?')
myName = input()
print('Great to meet you ' + str(myName))
print('The length of your name is: ')
print(len(myName))

# Ask user for their age
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')