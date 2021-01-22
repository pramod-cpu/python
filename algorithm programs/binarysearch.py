'''
author - Pramod
data - 21-1-2021
package - algorithm programs
title - binary search the word from a list
'''
try:
    def binary_search(list,element):
        start=0
        end=len(list)-1
        while start<=end:
            mid=(start+end)//2
            if element>list[mid]:
                start=mid+1
            elif element<list[mid]:
                end=mid-1
            else:
                return mid
        return -1
    f=open('file.txt')
    data=f.read().split()
    data.sort() 
    word = input('enter a word: ')
    res=binary_search(data,word)
    if res==-1:
        print('element not in the list')
    else:
        print('element is present at index:',res)

except FileNotFoundError:
    print('file is not recognized')