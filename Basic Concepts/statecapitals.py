'''
Created on Feb 28, 2012

@author: Ben Clauss, Meredith Hoo, Ryan Seffinger
'''
import sys
import random

state_dictionary = {}


def populate_dictionary():
    
    '''Opens statecapitals.csv and populates the state_to_capital dictionary
    with the values read from the file. Prints an error message and exits the
    program if an IOError occurs.
    
    Arguments:
    None
    
    Returns:
    None
    '''
    
    try:
        input_file = open("statecapitals.csv", "r")
    except IOError as error:
        print("I/O error(" + str(error.errno) + "): " + "statecapitals.csv" + ", " + error.strerror + ".")
        sys.exit(1)
    
    for line in input_file:
        lst = line.strip().split(",")
        state_dictionary[lst[0]] = lst[1]

def get_random_state():
    '''Chooses a random state from the dictionary's set of keys.
    
    Arguments:
    None
    
    Returns:
    The name of a state
    '''
    
    keylist = list(state_dictionary.keys())
    randkeynum = random.randint(1,len(keylist))
    randomstate = keylist[randkeynum]
    return randomstate

def play_again():
    '''Asks the user if he or she wants to play again. Repeats the question
    until the user answers 'y' or 'n'.
    
    Arguments:
    None
    
    Returns:
    A boolean containing the user's choice
    '''
    
    while True:
        again = input("Play again (Y/N)? ")
        if again.lower() == "y":
            return True
        elif again.lower() == "n":
            return False
        print()
        
def main():
    play = True
    populate_dictionary()
    print("--- Welcome to Guess the State Capital ---")
    while play:
        print("You get 3 tries...")
        randomstate = get_random_state()
        capital = state_dictionary[randomstate]
        for turn in range(1, 4):
            answer = input("What is the capital of " + str(randomstate) + "? ")
            if answer.lower() == capital.lower():
                print("You are correct!" + "\n")
                break
            elif answer.lower() != capital.lower():
                if turn == 1:
                    print("No. Try again.")
                elif turn == 2:
                    print("No. You get one more chance.")
                elif turn == 3:
                    print("No. The capital of " + str(randomstate) + " is " + str(capital) + "." + "\n")
        again = play_again()
        if not(again):
            print("Bye.")
            break

        
                

if __name__ == "__main__":
    main()