'''
author - Pramod
date - 21-1-2021
Title - sqrt to compute the square root of a nonnegative number
'''
import unittest
class Non_neg:
    def __init__(self):
        self.c = int(input('enter a positive number: '))
        self.epsilon = 1e-15
    def nonnegative(self):
        self.t=self.c
        while (abs(self.t - self.c / self.t) > self.epsilon * self.t):
            self.t = (self.c / self.t + self.t)/2
        return round(self.t,3)
class TestCase(unittest.TestCase):
    def test_nonnegative(self):
        test1=Non_neg()
        test2=Non_neg()
        self.assertEqual(test1.nonnegative(),1.414)
        self.assertEqual(test2.nonnegative(),10.0)
unittest.main()
