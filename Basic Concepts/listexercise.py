'''
Created on Jan 3, 2012

@author: Meredith
'''
import random

def get_user_input(message, datatype):
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
def create_list_of_random_ints(length, a, b):
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(a, b))
    return random_list
def find_max(lst):
    length = len(lst)
    if length == 0:
        raise ValueError("find_max() list is an empty sequence.")
    max_value = lst[0]
    max_index = 0
    for i in range(1, length):
        if lst[i] > max_value:
            max_index = i
            max_value = lst[i]
        if lst[i] != int(lst[i]):
            raise TypeError("cannot concatenate 'str' and 'float' objects.")
    return (max_value, max_index)#algorithm - sequence of steps that is taken to systematically solve a problem
                
def main():
    length = get_user_input("Enter list length: ", "int")
    random_list = create_list_of_random_ints(length, 1, 100)
    print(random_list)
    max_value = max(random_list)
    
if __name__== '__main__':
    main()