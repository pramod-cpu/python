'''
author - Pramod
data - 21-1-2021
package - algorithm programs
title - prime numbers from 0 to 1000 and program to find the prime numbers that are Anagram and
Palindrome.
'''

def prime_palindrome():
    l=[]
    for i in range(2,1001):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
    print(l)
    for i in l:
        temp=i
        rev=0
        while i>0:
            rev=rev*10+(i%10)
            i=i//10
        if rev==temp:
            print(temp)
prime_palindrome()

















