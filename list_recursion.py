'''
Created on May 7, 2012

@author: Meredith
'''
def power_helper(x, y):
    if y == 0:
        return 1
    return x** power_helper(x, y-1)


def sum_tail(lst, lower, upper):
    return sum_tail_helper(lst, lower, upper, 0)

def sum__tail_helper(lst, lower, upper, result):
    if lower > upper:
        return result
    return sum_tail_helper(lst, lower+1, upper, result+ lst[lower])
    
if __name__== "__main__":
    lst = [1,12, 2]