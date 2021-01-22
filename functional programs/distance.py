'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - Euclidean distance from 1 point to origin
'''

from sys import argv
from math import sqrt,pow
print('enter two integers (x,y):',argv)
args=argv[1:]
a,b=int(args[0]),int(args[1])
try:
    distance = sqrt(pow(a,a)+pow(b,b))
    print('Euclidean distance is:',distance)
except ValueError:
    print('provide integer input')
