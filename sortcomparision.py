'''
Created on Jan 27, 2012

@author: Meredith
'''
import random
import time
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

def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def bubble_sort(lst):
    n = len(lst)
    while n > 0:
        new_n = 0
        for i in range(1,n):
            if lst[i-1] > lst[i]:
                swap(lst, i - 1, i)
                new_n = i
        n = new_n  

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):#i is 
        min_index =  i
        for j in range(i + 1, n):
            if lst[j] <lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)
#n*(n-1)/2 number of comparisions            
def main():
    
    
if __name__== "__main__":
    main()