'''
author - Pramod
data - 21-1-2021
package - algorithm programs
title - Bubble sort
'''
def Bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
list=[5,7,3,2,8]
Bubblesort(list)
print(list)