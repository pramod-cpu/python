'''
author - Pramod
date - 21-1-2021
Title - monthly payment
'''

from sys import argv
from math import pow
print('enter year,principle loan,rate of interest:',argv)
Y,P,R=int(argv[1]),float(argv[2]),float(argv[3])
def monthly_payment():
    try:
        n = 12 * Y
        r = R/ (12*100)
        payment = ( P * r ) / (1-pow((1+r),-n))
        print('Monthly payment is:',round(payment,3))
    except ValueError:
        print("provide valid input")
monthly_payment()
