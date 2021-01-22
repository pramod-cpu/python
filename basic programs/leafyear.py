'''
author - Pramod
date - 20-1-2021
package - basic core programs
Title - propgram to check Leap Year
'''

def leapyear(year):
    try:
        if len(year)==4:
            if int(year)%4==0 and int(year)%100!=0 or int(year)%400==0:
                print(year,'is leap-year')
            else:
                print(year,'is not a leap-year')
        else:
            print('enter valid input')
    except ValueError:
        print('provide integer input')
year=input('Enter a year: ')
leapyear(year)
