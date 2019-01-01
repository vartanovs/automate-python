# This program counts the frequency of characters in a string
my_str = 'It was a bright cold day in April and the clocks were striking thirteen'
char_count_dict = {}

for c in my_str.lower():
  char_count_dict.setdefault(c, 0)
  char_count_dict[c] += 1 # No error because default was already set, ensuring the key exists

print(char_count_dict)
