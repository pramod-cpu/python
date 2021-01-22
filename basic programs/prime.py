'''
author - Pramod
date - 20-1-2021
package - basic core programs
Title - prime factors of number N
'''

def prime_factors(N):
    for i in range(2,N+1):
        if N%i==0:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
N=int(input('enter a number to check prime factors: '))
print('Prime factors of {} are: '.format(N))
prime_factors(N)
