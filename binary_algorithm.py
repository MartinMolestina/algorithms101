# Binary algorithm learning unit from khan academy
# Guessing a number using  binary algorithm

import random

#guessing a number example
def num_guess():
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

# guessing a prime number
def prime_num_search():
    # define search parameters
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
	41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    minim = 0
    maxim = len(primes) - 1
    guess = int((maxim-minim)/2)

    # input guess from user
    number = int(input('Guess a prime number between 0 and 100: '))

    # loop guessing values
    if number in primes:
        while primes[guess] != number:
            guess = int((maxim-minim)/2)
            print('The PC guesses: {}'.format(primes[guess]))
            
            if number > primes[guess]:
                print('The number is higher than {}.'.format(primes[guess]))
                minim = guess +1
            if number < primes[guess]:
                print('The number is lower than {}.'.format(primes[guess]))
                maxim = guess +1
             
            

    else:
        print('Number is not prime!')


prime_num_search()