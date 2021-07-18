import random

roll = random.randint(1,6)
guess = int(input('guess the dice roll?\n'))

if guess==roll:
  print('you guessed it right')
else:
  print('wrong. the value: ' + str(roll))  