# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:02:28 2021

"""

import numpy as np

# Przykład z zadania "na kartce"
# A = np.array([[999, 998], [1000, 999]], dtype=np.float32)
# B = np.array([[1997],[1999]], dtype=np.float32)
# Przykład z zadania wykładu z "9 rozdziałów o sztuce matematycznej"
A = np.array([[3,2,1],[2,3,1],[1,2,3]], dtype=np.float32)
B = np.array([[39],[34],[26]], dtype=np.float32)
# Przykład losowy
# A = np.random.randint(1, 10, (10, 10)).astype(np.float32)
# B = np.random.randint(1, 10, (10, 1)).astype(np.float32)

# Algorytm eliminacji Gaussa bez pivotingu generujący jedynki naprzekątnej macierzy U
for n in range(0, A.shape[0]):
    B[n][0] = B[n][0]/A[n][n]
    A[n,:] = A[n,:]/A[n][n]
    # Sprawdzenie czy macierz ma same jedynki na przekątnej (jeśli tak to algorytm powinnien zakonczyć działanie)
    if np.count_nonzero(np.diag(A) - 1) != 0:
        for m in range(n+1, A.shape[0]):
            B[m][0] = B[m][0] - B[n][0] * A[m,n]
            A[m,:] = A[m,:] - A[n,:] * A[m,n]
print("Wynik działania Algorytmu eliminacji Gaussa bez pivotingu generującego jedynki naprzekątnej macierzy. \n A={0} \n B={1}".format(A,B))

A = np.array([[3,2,1],[2,3,1],[1,2,3]], dtype=np.float32)
B = np.array([[39],[34],[26]], dtype=np.float32)

# Algorytm eliminacji Gaussa bez pivotingu nie generujący jedynekna przekątnej macierzy U
for n in range(0, A.shape[0] - 1):
    for m in range(n+1, A.shape[0]):
        B[m][0] = B[m][0] - B[n][0] * A[m,n] / A[n,n]
        A[m,:] = A[m,:] - A[n,:] * A[m,n] / A[n,n]
        
print("Wynik działania Algorytmu eliminacji Gaussa bez pivotingu nie generującego jedynek naprzekątnej macierzy. \n A={0} \n B={1}".format(A,B))

A = np.array([[3,2,1],[2,3,1],[1,2,3]], dtype=np.float32)
B = np.array([[39],[34],[26]], dtype=np.float32)

# Algorytm eliminacji Gaussa z pivotingiem
for n in range(0, A.shape[0] - 1):
    max_index = np.abs(A[n:,n]).argmax() + n
    B[[n, max_index]] = B[[max_index, n]]
    A[[n, max_index]] = A[[max_index, n]]
    for m in range(n+1, A.shape[0]):
        B[m][0] = B[m][0] - B[n][0] * A[m,n] / A[n,n]
        A[m,:] = A[m,:] - A[n,:] * A[m,n] / A[n,n]

print("Wynik działania Algorytmu eliminacji Gaussa z pivotingiem. \n A={0} \n B={1}".format(A,B))

A = np.array([[3,2,1],[2,3,1],[1,2,3]], dtype=np.float32)
B = np.array([[39],[34],[26]], dtype=np.float32)

# Algorytm LU faktoryzacji bez pivotingu
L = np.eye(A.shape[0], dtype=np.float32)
U = np.copy(A)
for n in range(0, A.shape[0] - 1):
    for m in range(n+1, A.shape[0]):
        L[m,n] = U[m,n] / U[n,n]
        U[m,:] = U[m,:] - L[m,n] * U[n,:] 
            
print("Wynik działania Algorytmu LU faktoryzacji bez pivotingu. \n L={0} \n U={1} \n L@U={2} \n A={3}".format(L,U,L@U,A))