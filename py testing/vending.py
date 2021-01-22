'''
author - Pramod
date - 20-1-2021
Title -Find the Fewest Notes to be returned for Vending Machine
'''
import unittest
class Currency:
    def countCurrency(self,amount): 
        notes = [1000,500,100,50,10,5,2,1]         
        noteCounter = [0, 0, 0, 0, 0, 0, 0, 0]
        print ("Currency Count:") 
        count=0
        for i, j in zip(notes, noteCounter): 
            if amount >= i: 
                j = amount // i 
                amount = amount - (j * i)
                count+=j
                print (i ," ----> ", j) 
        print('minimum number of notes to be returned:')
        return count
try:
    amount = int(input('enter an amount: '))
    if type(amount)==int:
        c=Currency()
        print(c.countCurrency(amount))
except Exception as err:
    print(err)

class TestCase(unittest.TestCase):
    def test_countCurrency(self):
        test1=Currency()
        test2=Currency()
        self.assertEqual(test1.countCurrency(1500),2)
        self.assertEqual(test2.countCurrency(1450),6)
unittest.main()