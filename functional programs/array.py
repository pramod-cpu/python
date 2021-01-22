'''
author - Pramod
date - 20-1-2021
package -functional programs
Title - 2D array
'''

M,N=[int(i) for i in input('enter no of rows and columns: ').split()]
Matrix=[]
for i in range(M):
    c=[]
    for j in range(N):
        j=int(input('Enter number at '+str(i)+' '+str(j)+' '))
        c.append(j)
    print()
    Matrix.append(c)
for i in range(M):
    for j in range(N):
        print(Matrix[i][j],end=' ')
    print()