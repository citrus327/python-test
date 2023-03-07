import sys, random

target = random.randint(1, 10)
print('Type your guess:')
guess = int(input())
guessingCount = 1
while True:
  if guessingCount >= 5:
    print('Sorry you guessed ' + str(guessingCount) + ' times, session expired')
    sys.exit()
  if target == guess:
    print('Congrats! you guessed ' + str(guessingCount) + ' times!')
    break
  elif guess >= target:
    print('You guessed too large')
  else:
    print('You guessed too small')
  
  guess = int(input())
  guessingCount+=1
