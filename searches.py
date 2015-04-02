'''
Created on Jan 11, 2012

@author: Meredith
'''
def linear_search(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

def binary_search(lst, key):
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
    lst = [10,14,15,16,17]
    index = binary_search(lst,14)
    print(index)
if __name__ == '__main__':
    main()