'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - program to find windchill
'''

from sys import argv
from math import pow
print('the number of command-line arguments:',argv)
args=argv[1:]

try:
    if int(args[0])<50 and (int(args[1])<120 and int(args[1])>3):
        w=35.74 + 0.6215*(int(args[0])) + (0.4275*(int(args[0]))- 35.75) * pow(int(args[1]),0.16)
        print('The windchill is:',w)
except ValueError:
    print('provide valid input')