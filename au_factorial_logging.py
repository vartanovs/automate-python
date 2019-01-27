import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG) # comment out to maintain DEBUG logging

logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s)' % (n))
  total = 1
  for i in range(n + 1): # There is a bug here! i starts at 0...
      total *= i
      logging.debug('i is %s, total is %s' % (i, total))
  logging.debug('Return value is %s' % (total))
  return total

num = 5

print(f'{str(num)} factorial is: ' + str(factorial(num)))

logging.debug('End of program')
