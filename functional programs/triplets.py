'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - Sum of three Integer adds to ZERO
'''

def findTriplets(arr, n): 
    found = True
    for i in range(0, n-2): 
        for j in range(i+1, n-1): 
            for k in range(j+1, n): 
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
    if (found == False): 
        print(" triplets not exist ") 
array = eval(input('Enter a list: ')) 
print(array)
n = len(array) 
findTriplets(array, n)