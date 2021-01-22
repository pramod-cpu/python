'''
author - Pramod
date - 20-1-2021
package - basic core programs
Title - power of 2
'''

from sys import argv
print('enter a command-line arguments:',argv)
args=int(argv[1])
try:
    if (args)<31:
        for i in range(args):
            print(2**i)
except ValueError:
    print('provide valid input')
else:
    print('provide Power value is between 0 to 31 only.')