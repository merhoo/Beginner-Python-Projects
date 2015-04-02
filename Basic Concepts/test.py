'''
Created on Mar 7, 2012

@author: Meredith
'''
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: Python " + sys.argv[0] + ' [name]') 
        sys.exit(1)
    print("Hello, " + sys.argv[1])