'''
Created on Oct 14, 2011
Due Tuesday, Oct 18, 2011

@author: Meredith Hoo, James Brancali, Kevin Mulligan
'''
import random

MAX_TRIES = 7
random_number = random.randint(1, 100)
counter = 1

print('''--- Welcome to 'Guess My Number' ---
      ''')
print('''I'm thinking of a number between 1 and 100.
try to guess the number in 7 attempts...''') #print statements

while counter <= MAX_TRIES: # while tries is not equal to MAX_TRIES than this will loop
    guess = int(input('Enter guess ' + str(counter)+ ': '))#asks user for number guess
    if guess == random_number:#if the guess is correct than it will break from program and congratulate the user
        if counter == 1:
            print()
            print('Congratulations, you correctly guessed the number ' + str(random_number) + ', and it took you only ' + str*(counter) + 'try')
            break
        else:
            print('Congratulations! You correctly guessed the number ' + str(random_number) + ', and it took you only ' + str(counter) + ' tries!')
            break
    elif guess > random_number:# if guess is lower, than it will tell the user it is lower
        print('    Lower...')
    elif guess < random_number:# if guesss is higher, than it will tell the user it is higher
        print('    Higher...')    
    if counter == MAX_TRIES:# if the user didn't guess correctly in the MAX_TRIES than it will tell the user sorry
        if MAX_TRIES == 1:
            print()
            print('Sorry, you did not guess the number ' + str(random_number) + ', in ' + str(MAX_TRIES) + ' try.')
        else:
            print('Sorry, you did not guess the number ' + str(random_number) + ', in ' + str(MAX_TRIES) + ' tries.')
    counter +=1# counter increments value by 1
    break