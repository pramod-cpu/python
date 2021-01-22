'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - stop watch program
'''

import time
start=time.time()
for i in range(10000):
    print(i,end=' ')
end=time.time()
print('\nelapsed time is:',end-start)