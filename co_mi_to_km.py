# This program converts kilometers to miles

# Constant Kilometer to Mile Conversion
MILE_TO_KM = 0.62

# Prompt user for a numerical kilometer distance
print('How many kilometers did you run today?')
try:
  kms = float(input())
except:
  # Trigger loop in case of invalid input
  print('Please enter a number')
  while True:
    try:
      kms = float(input())
      break
    except:
      pass

# Convert user's kilometer input to miles with 2 significant digits ... and print
mi = round(kms * MILE_TO_KM, 2)

print(f'Your {kms}km run was {mi}mi.')
