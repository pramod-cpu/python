'''
author - Pramod
data - 21-1-2021
package - algorithm programs
title - program to check angarams
'''

def anagrams(s1,s2):
    if sorted(s1)==sorted(s2):
        print(s1,'and',s2,'are anagrams')
    else:
        print(s1,'and',s2,'are not anagrams')
s1=input('Enter a first string: ')
s2=input('Enter a second string: ')
anagrams(s1,s2)