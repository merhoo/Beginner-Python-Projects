'''
Created on Jan 24, 2012

@author: Meredith
'''
def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    '''
    '''
    
def bubble_sort(lst):
    n = len(lst)
    while n > 0:
        new_n = 0
        for i in range(1,n):
            if lst[i-1] > lst[i]:
                swap(lst, i - 1, i)
                new_n = i
        n = new_n
    '''
    '''
        
def bubble_sort2(lst):
    n = len(lst)
    p = 1
    x = False
    while not(x) and p < n:
        x = True
        for i in range(0, n - p):
            if lst[1] > lst[i+1]:
                swap(lst, i, i+1)
                x = False
        p += 1
    '''
    '''
        
#n*(n-1)/2 number of comparisions
def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_index =  i
        for j in range(i+ 1, n):
            if lst[j] <lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)
    '''
    '''
                
def main():
    lst = [10,14,15,16,17]
    index = bubble_sort2(lst)
    print(index)
    
if __name__ == '__main__':
    main()