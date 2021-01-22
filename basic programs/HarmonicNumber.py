'''
author - Pramod
date - 20-1-2021
package - basic core programs
Title - to find nth Harmonic Number
'''

def harmonic_number(N):
    if N!=0:
        h1=1
        for i in range(2,N+1):
            h1=h1+(1/i)
        print('{} th harmonic number is:{}'.format(N,h1))
    else:
        print('N should not be equal to zero')
N=int(input('Enter a number: '))
harmonic_number(N)