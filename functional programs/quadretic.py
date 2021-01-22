'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - program on Quadratic  equation.
'''

from math import sqrt
def quadratic(a,b,c):
    try:
        delta = sqrt(b*b - 4*a*c)
        Root1= (-b + delta)/(2*a)
        Root2= (-b - delta)/(2*a)
        return Root1,Root2
    except ValueError:
        print('provide valid input')
a,b,c=[int(i) for i in input('enter a,b,c values: ').split(',')]
print('value of known variable is:',quadratic(a,b,c))