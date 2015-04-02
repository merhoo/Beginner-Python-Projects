'''
Created on May 7, 2012

@author: Meredith
'''
def fact_tail(n):
    return fact_helper(n, 1)

def fact_helper(n, total):
    if n == 0:
        return total
    return fact_helper(n-1, n*total)

def fact(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is not an integer.")
    if n < 0:
        raise ValueError("Factorial must be a positive integer")
    return n

if __name__=="__main__":
    n = fact(100)
    print(n)
    n= fact_tail(100)
    print(n)