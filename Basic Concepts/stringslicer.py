'''
Created on Nov 8, 2011

@author: Meredith
'''
import sys

string = input('Enter a string up to 99 characters long: ').strip()
strlen = len(string)
if strlen == 0:
    print('Error: String is empty')
    sys.exit(1)
elif strlen > 99:
    print('Error: String is ', strlen -99, ' characters too long.')
    sys.exit(1)
    

while True:
    print()
    print(' ', end = '')
    for i in range(strlen +1):
        print(i, end = '')
        ilength = len(str(i))
        if i != strlen:
            for j in range(4 - ilength):
                print(' ', end = '')
    print()

    print(' ', end = '')
    for i in range(strlen + 1):
        if i != strlen:
            print('+---', end = '')
        else:
            print('+', end = '')
    print()

    print(' ', end = '')
    for i in range(strlen):
        print('| ' + string[i] + ' ', end = '')
    print('|')
   
    print(' ', end = '')
    for i in range(strlen):
        if i != strlen:
            print('+---', end = '')
        else:
            print('+', end = '')
    print()
   
    for i in range(-strlen, 0):
        print(i, end = '')
        ilength = len(str(i))
        if i != strlen:
            for j in range(4 - ilength):
                print(' ', end = '')
    print('\n')  
   
    start_str = input('Start: ').strip()
    if len(start_str) == 0:
        break
    finish_str = input('Finish: ').strip()
    if len(finish_str) == 0:
        break
    start = int(start_str)
    finish = int(finish_str)
    print('string[' + str(start) + ':' + str(finish) + "] is '" + string[start:finish] + "'")
    
print('Bye')