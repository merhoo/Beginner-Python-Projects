import subprocess
import os
import random
import time
import sys

#START definitions

#clearscreen
if os.name == 'nt':
    def clearscreen():
        subprocess.call("cls", shell=True)
        return
else:
    def clearscreen():
        subprocess.call("clear", shell=True)
        return

def printing(): #print out the "_ _ a _ _"
    for i in to_print:
        print(i, end=' ')

def anamation(): #ASCII anamation at the end
    for counting in range(7):
        clearscreen()
        print('- - -')
        time.sleep(.1)
        clearscreen()
        print('/ / /')
        time.sleep(.1)
        clearscreen()
        print('| | |')
        time.sleep(.1)
        clearscreen()
        print("""\ \ \ """)
        time.sleep(.1)

#words to choose from
ALL_WORDS = ('software', 'hardware', 'mac', 'windows', 'phone', 'mouse', 'keyboard', 'apple', 'microsoft', 'java', 'python', 'javascript',\
'printer', 'motherboard', 'game', 'battery', 'intel', 'amazon', 'desktop', 'laptop', 'calculator', 'science', 'speaker', 'monitor')

ran_num = random.randrange(len(ALL_WORDS)) #generate random number for point in list of words
word = ALL_WORDS[ran_num] #pick word from list

to_print = '' #the "_ _ a _"
for i in range(len(word)): #makes to_print
    to_print += '_'

letters_left = len(to_print)

locations = [] #store location that user chose (e.g., a is 5 in _ _ _ _ _)
guessed = [] #store recently guessed letters 

guess_num = 1
score = 0

print("""Welcome to... WORD GUESS
(Press Enter To Exit)\n""")

printing()
print()

while True:
    if guess_num > 19: #check if user guessed too much
        clearscreen()
        print('I\'m sorry, you ran out of guesses')
        input('\nPress enter to exit...')
        sys.exit(0)

    print('\nLetters:         ' + str(letters_left))
    print('Score:           ' + str(score))
    print('Guess:           ' + str(guess_num))
    guess_num += 1
    print()
    guess_letter = input('Enter a letter/word: ')
    
    if len(guess_letter) > 1: #user guess a word
        if guess_letter == word: #if word is correct
            score += 10 * (20 - guess_num)
            clearscreen()
            print('CORRECT!!!!')
            print('Score = ' + str(score))
            input('Press enter to quit...')
            sys.exit(0)
        else: #if word is wrong
            print('I\'m sorry, that was incorrect.')
            score -= 30

    elif guess_letter == '': #if user just pressed enter
        clearscreen()
        print('I guess this was too challenging for you...')
        input('\nPress Any Key To Exit...')
        sys.exit(0)

    else: #if user guessed one letter
        already_guessed = False
        clearscreen()
        
        for i in guessed: #check if already guessed letter
            if guess_letter == i:
                print('You already guessed that...')
                already_guessed = True
                break

        if not(already_guessed): #if new guess
            correct = False
            
            for i in range(len(word)): #check to see if correct
                if word[i] == guess_letter:
                    correct = True
                    locations.append(i)
                    score += 10
            guessed.append(guess_letter)
            if correct == False:
                score -= 15

        for i in locations: #change to_print
            to_print = to_print[:i] + word[i] + to_print[i + 1:]

        #calculate letters left
        letters_left = 0
        for character in to_print:
            if not(character.isalpha()):
                letters_left += 1
        
        printing()
        print()

    if to_print == word: #if all letters were guessed
        score += 20
        anamation()
        print('Your score is: ' + str(score))
        input('Press enter to quit... ')
        sys.exit(0)
    