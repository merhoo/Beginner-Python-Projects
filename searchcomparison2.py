'''
Created on Jan 23, 2012

@author: merhoo
'''

import time
import random

def get_user_input(message, datatype):
    '''Prompts the user to enter a value of the specified datatype until no
    errors occur and a value is obtained

    Arguments:
    message -- the prompt that is seen by the user
    datatype -- the type of data the value is expected to be; either int,
                float, or str

    Returns:
    A value
    '''
    str_input = input(message).strip() # From user input, gets the value
    output = 0
    if str_input == '':
        raise ValueError("Error: Received no input.")# Switches ValueError into TypeError
    
    try: # Checks if the key entered is an int
        if datatype == 'int':
            output = int(str_input)
    except ValueError:
        raise TypeError("Error: '" + str(str_input) + "' is not of type " + datatype + ".")

    return output # If user_input is invalid, raises Error. Else, returns the key

def create_list_of_random_ints(length, a, b, sort=False):
    '''Creates a list of random integers.

    Arguments:
    length -- the length of the list to create
    a      -- the minimum value in the list
    b      -- the maximum value in the list
    sort   -- whether or not the list should be sorted; default is False

    Returns:
    A list of integers
    '''
    random_list = []
    for i in range(length):
        random_list.append(random.randint(a, b))
    random_list.sort()
    return random_list

def linear_search(lst, key):
    '''Searches the lst for key.

    Arguments:
    lst -- the list to search
    key -- the value to search for

    Returns:
    The index of the first occurrence of key in lst
    -1 if index is not in lst
    '''
    length = len(lst)

    for i in range(length):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst, key):
    '''Searches the lst for key.

    Arguments:
    lst -- the sorted list to search
    key -- the value to search for

    Returns:
    The index of key in lst, or -low - 1, if the key is not present. The
    caller of this function can convert index = -low - 1 to a positive index
    indicating where the key would be inserted by using the value -index - 1.
    '''
    high = len(lst) - 1 # Sets high value, low value, and middle value in list
    low = 0
    
    while high >= low:
        current = low + (high - low)//2
        if key < current:
            high = current - 1
        elif key > current:
            low = current + 1
        elif key == current:
            return current
        return - low - 1

def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def main():
    print("--- Linear Binary/Search Comparison ---")
    print()
    list_length = -1
    num_keys = -1

    while list_length < 0 or num_keys < 0:
        list_length = get_user_input("Enter list size: ", "int")
        num_keys = get_user_input("Enter number of keys: ", "int")
        if list_length < 0 or num_keys < 0:
            print("List size and/or number of keys cannot be negative")
    
    main_list = create_list_of_random_ints(list_length, 0, 1000000, True)
    key_list = create_list_of_random_ints(num_keys, 0, 1000000)
    key_length = len(key_list)
    print("Running linear search...", end = "")
    t1 = time.time()

    for i in range(0,key_length):
        found_it = linear_search(main_list, key_list[i])
        #print("Linear search return value: ", found_it)
    
    t2 = time.time()
    print("done.")
    print ("Elapsed time for linear search: %s seconds." %(str(t2-t1)))
    print("Running binary search...", end = "")
    t1 = time.time()
    
    for i in range(0,key_length):
        found_it = binary_search(main_list, key_list[i])
        #print("Binary search return value: ", found_it)
        
    t2 = time.time()
    print("done.")
    print("Elapsed time for binary search: %s seconds." %(str(t2-t1)))


if __name__=='__main__':
    main()
