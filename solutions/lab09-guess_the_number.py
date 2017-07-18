
# 1) the computer will pick a random number between 1 and 10
# 2) the user will try to guess that number
# 3) if the guess is correct, tell the user "that's correct!"
# 4) otherwise, tell the user "that's incorrect!"

# step 2
# compare the target and guess
# if the target is greater than the guess, print 'higher'
# otherwise, print 'lower'

import random

target = random.randint(1,10)

guess = ''
while True:
    guess = input('guess the number! ')
    guess = int(guess)
    if guess == target:
        print('that\'s correct!')
        break
    else:
        print('that\'s incorrect!')

    if target > guess:
        print('guess higher!')
    else:
        print('guess lower!')

