'''
Created on Jan 20, 2012

@author: Meredith
'''
import time
import random
def get_user_input(message, datatype):
    '''Prompts the user to enter a value of the specified datatype until no errors occur and a value is obtained.
    Arguments:
    message -- the prompt that is seen by the user
    datatype -- the type of data the value is expected to be; either int, float or str
    
    Returns:
    A value
    '''
    while True:
        str_input = input(message).strip() 
        if datatype == 'int':
            try:
                return int(str_input)
            except ValueError:
                print("Error: Input '" + str_input + " ' is not of type " + datatype + ".")
        elif datatype == 'float':
            try:
                return float(str_input)
            except ValueError:
                print("Error: Input '" + str_input + " ' is not of type " + datatype + ".")
        else:
            return str_input
def create_list_of_random_ints(length, a , b, sort=False):
    '''Creates a list of random integers.
    
    Arguments:
    length -- the length of the list to create
    a -- the minimum value in the list 
    b -- the maximum value in the list
    sort -- whether or not the list should be sorted, default is False
    
    Returns:
    The index of the first occurrence of a key in lst
    '''
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(a, b))    
    if sort == False:
        random_list.sort
    return random_list
def binary_search(lst, key):
    '''Searches the lst for key.
    
    Arguments:
    lst -- the list of to search
    key -- value to search for
    
    Returns:
    The index of key n lst, or -low - 1, if the key is not present.
    The caller of this function can convert index = -low -1 to a positive 
    index indicating where the key would be inserted by using the value -index - 1.
    '''
    low = 0
    high = len(lst) -1
    while high >= low:
        mid = low + (high - low)//2
        if key == lst[mid]:
            return mid
        if key > lst[mid]:
            low = mid + 1
        if key < lst[mid]:
            high = mid - 1
    return -low - 1

def main():
    print("--- Linear Binary/Search Comparison")
    list = input(int('Enter list sizze: '))
    key = input(int('Enter number of keys: '))
    start = time.clock()
    print('Elapsed time for linear search: ', time.clock() - start)
    print('Elapsed time for binary search: ', time.clock() - start)
if __name__ == '__main__':
    main()