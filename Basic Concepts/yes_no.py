'''
Created on Dec 12, 2011

@author: Meredith
'''
def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False