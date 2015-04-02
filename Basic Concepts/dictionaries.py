'''
Created on Feb 27, 2012

@author: Meredith
'''
dictionary = {}
letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    index = 1
    for c in letters:
        dictionary[c] = index
        index += 1
    dictionary['a'] = 0
    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary["z"])
    

if __name__ == "__main__":
    main() ""