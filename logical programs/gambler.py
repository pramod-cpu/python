'''
author - Pramod
date - 20-1-2021
package -Logical programs
Title - gambler
'''

import random
stake,goal,trials=[int(i) for i in input('enter stake,goal,trails: ').split(',')]
bets = wins = 0
for t in range(trials):
    cash = stake
    while cash > 0 and cash < goal:
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
print(str(100 * wins//trials) + '% wins')
print('Avg results: ' + str(bets//trials))


