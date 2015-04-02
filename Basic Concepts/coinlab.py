'''
Created on Oct 5, 2011

@author: Meredith
'''
import random #to use random.random() 
import sys # to use sys.exit

print("Let's flip a coin...") #output lets flip coin
user_input = input('Enter heads or tails: ') #output tells user to input heads or tails
heads_selected = False

if user_input == 'heads':
    heads_selected = True
elif user_input == 'tails':
    heads_selected = False
else:
    print('Error: You must enter heads or tails. Please rerun the program')
    sys.exit(1)
    
random_number = random.random()
if random_number < 0.5:
    print('Coin flipped: heads')
else:
    print('Coin flipped: tails')
    
if heads_selected == True and random_number < 0.5:
    print('You Win!')
elif heads_selected == False and random_number >= 0.5:
    print('You Win!')
else:
    print('Sorry, you lose!')
    