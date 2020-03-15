#Program nalazi najmanji broj karaktera cijom transformacijom se od niske A dobija niska B
import numpy as np
A=input()
n=len(A)
B=input()
m=len(B)
C=np.zeros((n+1,m+1))
for i in range(n+1):
    C[i][0] = i
for j in range(m+1):
    C[0][j] = j
for i in range(1,n+1):
    for j in range(1,m+1):
        x = C[i-1][j]+1
        y = C[i][j-1]+1
        if A[i-1]==B[j-1]:
            z=C[i-1][j-1]
        else:
            z=C[i-1][j-1]+1
        C[i][j]= min(x,y,z)
print(int(C[n][m]))
