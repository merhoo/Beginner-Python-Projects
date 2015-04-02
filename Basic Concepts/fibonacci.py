'''
Created on May 7, 2012

@author: Meredith
'''
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    if n <= 0:
        raise TypeError("Tnput must be greater than 0")
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    