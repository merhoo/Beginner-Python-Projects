'''
Created on Feb 28, 2012

@author: Meredith
'''
import sys
import random
state_dictionary = {}

def populate_dictionary():
    '''Opens statecapitals.csv and populates  the state_to_capital dictionary
    with the values read the files. Prints an error message and exists the 
    program if an IOError occurs.
    
    Arguments:
    None
    
    Returns:
    None
    '''
    
    try:
        text_file = open("statecapitals.csv", "r")
    except IOError as error:
        print("Error: Cannot open '" + "statecapitals.csv" + "' for processing.")
        sys.exit(1)
    for line in text_file:
        capital = line.strip().split(",")
        state_dictionary[capital[0]] = capital[1]
    text_file.close()
def get_random_state():
    '''Choose a random state from the dictionary's set of keys.
    
    Arguments:
    None
    
    Returns:
    The name of the state.
    '''
    keys = list(state_dictionary.keys())
    random_key_num = random.randint(len(keys))
    random_state = keys[random_key_num]
    return random_state
def play_again():
    ''' Asks the user of he or she wants to play again. Repeats the question
    until the user answers 'y' or 'n'.
    
    Arguments:
    None
    
    Returns:
    A boolean containing the user's choice.
    '''
    while True:
        again = input("Play again(Y/N)? ")
        if again.lower() == "y":
            return True
        elif again.lower() == 'n':
            return False
def main():
    populate_dictionary()
    print("--- Welcome to Guess the State Capital ---")
    while True:
        print("You get 3 tries...")
        randomstate = get_random_state()
        for turn in range(1,4):
            answer = input(str("What is the capital of " + randomstate + "? "))
            if answer == random_state():
                print("Would you like to play again")
    
if __name__ == "__main__":
    main()