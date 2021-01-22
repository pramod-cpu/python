'''
author - Pramod
date - 21-1-2021
Title - program to find decimal to binary
'''

class Binary():
    def __init__(self,num):
        self.num=num
    @property
    def toBinary(self):
        s=''
        while self.num>0:
            s=s+str(self.num%2)
            self.num=self.num//2
        return '{}'.format(s[::-1])
num=int(input('Enter decimal number: '))
try:
    if type(num)==int:
        b=Binary(num)
except ValueError:
    print('provide valid input')
import unittest
class TestBinary(unittest.TestCase):
    def test_toBinary(self):
        test1=Binary(10)
        test2=Binary(24)
        self.assertEqual(test1.toBinary,'1010')
        self.assertEqual(test2.toBinary,'11000')
if __name__=='__main__':
    unittest.main()