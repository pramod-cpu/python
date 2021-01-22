'''
author - Pramod
data - 22-1-2021
package - algorithm programs
title - selection sort
'''

def selectionsort(list):
    for i in range(5):
        min_pos=i
        for j in range(i,6):
            if list[j] < list[min_pos]:
                min_pos=j
        list[i],list[min_pos] = list[min_pos],list[i]
        print(list)
list=[5,7,3,2,8,1]
selectionsort(list)
print(list)