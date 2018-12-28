# Sum all numbers from 0 to n, exclusive

# Prompt user for a number
print('Please provide a positive integer:')
n = input()

# Declare a placeholder 'total' and sum numbers 0 to n using a for loop
total1 = 0
for num in range(int(n) + 1):
  total1 += num

print('The sum of numbers from 0 to ' + str(int(n)) + ' is ' + str(total1) + '.')

# Sum numbers using a while loop
i = 1
total2 = 0
while i <= int(n):
  total2 += i
  i += 1

print('Again, the sum of numbers from 0 to ' + str(int(n)) + ' is ' + str(total2) + '.')

# Use a more efficient algorithm to calculate the sum
total3 = (int(n) * (int(n) + 1)) / 2

print('Once again, the sum of numbers from 0 to ' + str(int(n)) + ' is ' + str(int(total3)) + '.')