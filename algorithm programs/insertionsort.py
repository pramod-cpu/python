'''
author - Pramod
data - 21-1-2021
package - algorithm programs
title - insertion sort
'''

def insrtion_sort(list):
    for i in range(1,len(list)):
        element=list[i]
        pos=i
        while element<list[pos-1] and pos>0:
            list[pos]=list[pos-1]
            pos=pos-1
        list[pos]=element
list=eval(input('Enter a list: '))
insrtion_sort(list)
print(list)


