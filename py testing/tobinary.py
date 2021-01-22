'''
author - Pramod
date - 21-1-2021
Title - program to find decimal to binary and swap the nibbles then check number is power of 2 or not
'''

import unittest
class Binary:
    def __init__(self,n):
        self.n=n
    def toBinary(self):
        a=bin(self.n)        #0b binary format
        b=a[2:]
        a=b.zfill(8)    # adds zero at left hand side
        first,second=a[:len(a)//2],a[len(a)//2:]
        first,second=second,first
        self.dec=first+second

    def toDecimal(self):
        self.sum=0
        j=len(self.dec)-1
        for i in self.dec:
            if int(i)==1:
                self.sum = self.sum+(2**j)
            j=j-1
        print(self.dec,'decimal value is: ',self.sum)     # self.sum is decimal number
        self.num = self.sum

    def power_0f_2(self):
        if self.num==0:
            return False
        while self.num!=1:
            if self.num%2!=0:
                return False
            self.num = self.num // 2
        return True
try:
    n=int(input('Enter decimal number: '))
    if type(n)==int:
        b=Binary(n)
        b.toBinary()
        b.toDecimal()
        print(b.power_0f_2())
except ValueError:
    print('provide valid input')

class TestCase(unittest.TestCase):
    def test_power_of_2(self):
        test1=Binary(4)
        test2=Binary(20)
        self.assertEqual(test1.power_0f_2(),True)
        self.assertEqual(test2.power_0f_2(),False)
unittest.main()













