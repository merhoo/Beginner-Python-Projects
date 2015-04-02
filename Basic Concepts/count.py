'''
Created on Jan 17, 2012

@author: Meredith
'''
def count(lst, key):
    '''returns how many times value is in list'''
    how_many = 0
    for value in lst:
        if value == key:
            how_many += 1
        return how_many
    
def remove_duplicates(lst):
    '''removes the duplicates in a list, returns the list without duplicates'''
    duplicate_lst = []
    for i in lst:
        if not i in duplicate_lst:
            duplicate_lst.append(i)
    duplicate_lst.sort
    return duplicate_lst


def main():
    lst = input('Enter a list: ')
    lst = count(lst)
    print(lst)
    lst = remove_duplicates(lst)
    print(lst)
    
if __name__ == '__main__':
    main()