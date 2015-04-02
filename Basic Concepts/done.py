'''
Created on Oct 11, 2011

@author: Meredith
'''
is_done = False
while not(is_done):
    answer = input('Are you done?')
    if answer == 'yes':
        print('Thank you for finishing')
        is_done = True
    elif answer == 'no':
        print('HURRY UP!')
    else:
        print('Excuse me?!?') 