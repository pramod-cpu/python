'''
author - Pramod
date - 21-1-2021
Title - temperature conversion
'''

import unittest
class Tempearature:
    def convert(self):
        try:
            self.fahrenheit = eval(input('enter a temperature in fahrenheit: '))
            if type(self.fahrenheit)==float or type(self.fahrenheit)==int:
                Celsius=  (self.fahrenheit -32)* (0.55)
                self.fahrenheit = (Celsius * 1.8) + 32
                return round(self.fahrenheit,3),round(Celsius,3)
        except (ValueError,NameError):
            print('provide valid input')
# t=Tempearature()
# print(t.convert())
class TestCase(unittest.TestCase):
    def test_convert(self):
        test1=Tempearature()
        test2=Tempearature()
        self.assertEqual(test1.convert(),(20.12,-6.6))
        self.assertEquals(test2.convert(),(1.31,-17.05))
unittest.main()

