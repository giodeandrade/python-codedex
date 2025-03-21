
# Dice Roll

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2

guess = int(input('What is the total (2-12)? '))

while guess != total:
  print("Nope, try again!")
  guess = int(input('What is the total (2-12)? '))

if guess == total:
  print("Congrats! You're right!")
