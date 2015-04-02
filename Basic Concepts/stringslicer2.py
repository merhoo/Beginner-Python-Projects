'''
Created on Dec 14, 2011

@author: Meredith
'''
import sys


string = input('Enter a string up to 99 characters long: ').strip()
strlen = len(string)

#sees if user input is valid
def get_string_from_user():
    if strlen == 0:
        print('Error: String is empty')
        sys.exit(1)
    elif strlen > 99:
        print('Error: String is ', strlen -99, ' characters too long.')
        sys.exit(1)
    return string

#displays the positive index values used to represent each character
def display_positive_indices(string):
    print()
    print(' ', end = '')
    for i in range(strlen +1):
        print(i, end = '')
        ilength = len(str(i))
        if i != strlen:
            for j in range(4 - ilength):
                print(' ', end = '')
    print()

#displays the 
def display_line(string):
    print(' ', end = '')
    for i in range(strlen + 1):
        if i != strlen:
            print('+---', end = '')
        else:
            print('+', end = '')
    print()
#displays the lines and 
def display_values(string):
    print(' ', end = '')
    for i in range(strlen):
        print('| ' + string[i] + ' ', end = '')
    print('|')

#displays the negative index values used to represent each character
def display_negitive_indices(string):
    for i in range(-strlen, 0):
        print(i, end = '')
        ilength = len(str(i))
        if i != strlen:
            for a in range(4 - ilength):
                print(' ', end = '')
    print('\n')  
   
def main():
    string = get_string_from_user()
    while True:
        display_positive_indices(string)
        display_line(string)
        display_values(string)
        display_line(string)
        display_negitive_indices(string)
        
        start_str = input('Start: ').strip()
        if len(start_str) == 0:
            break
        finish_str = input('Finish: ').strip()
        if len(finish_str) == 0:
            break
        start = int(start_str)
        finish = int(finish_str)
        print("string[" + str(start) + ":" + str(finish) + "] is '" + string[start:finish] + "'")
    print('Bye.')
    
if __name__ == '__main__':
    main()
    