# Binary algorithm learning unit from khan academy
# Guessing a number using  binary algorithm

import random

# Gathering user initial input
max = int(input('What is the highest possible number the computer is thinking of? '))
min = 0
number = random.randint(min, max)

# Guessing

while True:
    guess = int(input('Guess a number between {} and {}: '.format(min, max)))
    if guess == number:
        print('You guessed it !!!  You won !!!')
        break

    if guess > number:
        print ('Too high!')
        max = guess - 1

    if guess < number:
        print ('Too high!')
        min = guess + 1