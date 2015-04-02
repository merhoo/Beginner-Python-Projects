'''
Created on Jan 6, 2012
@author: Meredith Hoo, James Brancale, Jiwon Lee
'''

import math

def get_user_list(message, datatype):
    '''Prompts the user to enter a list of values of the specified datatype.
    Raises ValueError if there is no input or TypeError if the list contains
    elements of the wrong type.

    Arguments:
    message  -- the prompt that is seen by the user
    datatype -- the type of data each element is expected to be; either "int",
                "float", or "string"
                
    Returns:
    A list of values
    '''
    str_input = input(message).strip().split()#user input, creates a list
    output = []
    if len(str_input) == 0:
        raise ValueError("Error: Received no input.")#switches ValueError into TypeError
    
    for i in str_input:#see if each element is a int or float
        try:
            if datatype == 'int':
                output.append(int(i))
            elif datatype == 'float':
                output.append(float(i))
        except ValueError:
            raise TypeError("Error: Element '" + str(i) + "' is not of type " + datatype + ".")
        
    return output# if user_input is invalid, prints error 
    
def mean(lst):
    '''Computes the mean of a list of numbers.

    Arguments:
    lst -- the list of numbers, either ints or floats

    Returns:
    The mean value of the list
    '''
    num_sum = 0 # sum of numbers in list 
    for x in lst:
        num_sum += x
    return num_sum/len(lst) #create average

def std_dev(lst):
    '''Computes the standard deviation of a list of numbers.

    Arguments:
    1st -- the list of numbers, either ints or floats

    Returns:
    The standard deviation of values in the list
    '''
    num_mean = mean(lst) #mean
    num_sum = 0
    for x in lst:
        num_sum += (x - num_mean)*(x - num_mean)
    num_sum /= len(lst)
    num_sum = math.sqrt(num_sum)
    return num_sum
        

def main():
    while True:
        try:
            input_list = get_user_list("Enter integers, each separated by a space: ", "int")
        except (ValueError, TypeError) as error:
            print(error)
            continue
        break
    print()
    print("List: " + str(input_list))
    average = mean(input_list)
    print("Mean: " + str(average))
    deviation = std_dev(input_list)
    print("Standard deviation: " + str(deviation))
if __name__ == '__main__':
    main()