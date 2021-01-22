'''
author - Pramod
date - 20-1-2021
package - basic core programs
Title -Flip Coin and print percentage of Heads and Tails
'''

import random
N=int(input('Enter how many times do you want to flip a coin? '))
heads, tails = 0, 0
i = 0 
while i<N:
	coin_flips = random.randint(0,1)
	if coin_flips>0.5:
		heads += 1
	else:
		tails += 1
	i += 1
print(f"Out of {N} flips, head percentage is" + str((heads/N)*100) + " and tails percentage is:" + str((tails/N)*100))