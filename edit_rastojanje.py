#Program nalazi najmanji broj edit operacija kojim se od niske A dobija niska B
# npr abbc i babb, program ce vratiti 2 jer mozemo dopisati *b*abbc i potom ukloniti poslednje c
import numpy as np
def rastojanje(A,B):
    n = len(A)
    m = len(B)
    matrix = np.zeros((n + 1, m + 1))
    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = matrix[i - 1][j] + 1
            y = matrix[i][j - 1] + 1
            if A[i - 1] == B[j - 1]:
                z = matrix[i - 1][j - 1]
            else:
                z = matrix[i - 1][j - 1] + 1
            matrix[i][j] = min(x, y, z)
    return int(matrix[n][m])



