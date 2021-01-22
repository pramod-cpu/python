'''
author - Pramod
data - 22-1-2021
package - algorithm programs
title - Customize Message Demonstration using String Function and RegEx
'''
import re   
import datetime
name=input('enter your name: ')
fullname=input('enter your full name: ')
mob=input('enter your mobile number: ')
match1=re.fullmatch('[a-zA-Z]',fullname)
match2=re.fullmatch('[6-9]\d{9}',mob)
if match1!=None and match2!=None:
    print(f'''Hello <<{name}>>, We have your full name as <<{fullname}>> in our system. your contact number is 
            91-{mob}. Please,let us know in case of any clarification Thank you BridgeLabz {datetime.datetime.now()}.''')
else:
    print('provide valid input')