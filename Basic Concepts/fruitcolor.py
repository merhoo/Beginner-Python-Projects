'''
Created on Mar 9, 2012

@author: Meredith Hoo
'''
import sys
fruit_to_color = {}

def populate_dictionary():
    '''Opens fruitcolors.csv and populates the fruit_to_color dictionary
    with the values read from the file. All values are converted to lower
    case before being inserted in the dictionary. Prints an error message
    and exits the program is an IOError occurs.
    
    Arguments:
    None
    
    Returns:
    None
    '''
    try:
        input_file = open("fruitcolors.csv", "r")
    except IOError as error:
        print("I/O error(" + str(error.errno) + "): " + "fruitcolors.csv" + ", " + error.strerror + ".")
        sys.exit(1)
    for line in input_file:
        lst = line.lower().strip().split(",")
        fruit_to_color[lst[0]] = lst[1]
        
def main():
    populate_dictionary()
    if len(sys.argv) != 2:
        print("Usage: Python " + sys.argv[0] + ' [fruit name]') 
        sys.exit(1)
    user_input = input(str("python fruitcolor. py "))
    if user_input not in sys.argv:
        print(user_input.upper() + "not found in database.")
        
    print(" " + sys.argv[1])
    
if __name__=="__main__":
    main()