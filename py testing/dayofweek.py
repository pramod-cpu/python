'''
author - Pramod
date - 21-1-2021
Title - dayofweek
'''

from sys import argv
print('enter date,month,year:',argv)
dict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thrusday',5:'Friday',6:'saturday'}
args=argv[1:]
try:
    d,m,y=int(args[0]),int(args[1]),int(args[2])
    y0 = y - (14-m)//12
    x = y0 + (y0//4) - (y0//100) + (y0//400)
    m0 = m + 12 * ((14-m)//12)-2
    d0=(d + x + 31 * m0 // 12) % 7
    print('day of the week is:',dict[d0])
except ValueError:
    print('provide valid input')


    
