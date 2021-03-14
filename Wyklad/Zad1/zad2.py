# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:02:28 2021

"""

import numpy as np

# Przykład z zadania "na kartce"
# A = np.array([[[999, 998], [1000, 999]]], dtype=np.float32)
# B = np.array([[1997],[1999]], dtype=np.float32)
# Przykład z zadania wykładu z "9 rozdziałów o sztuce matematycznej"
# A = np.array([[3,2,1],[2,3,1],[1,2,3]], dtype=np.float32)
# B = np.array([[39],[34],[26]], dtype=np.float32)
# Przykład losowy
A = np.random.randint(0, 10, (10, 10)).astype(np.float32)
B = np.random.randint(0, 10, (10, 1)).astype(np.float32)

#Algorytm eliminacji Gaussa bez pivotingu generujący jedynki naprzekątnej macierzy U
for n in range(0, A.shape[0]):
    B[n][0] = B[n][0]/A[n][n]
    A[n,:] = A[n,:]/A[n][n]
    # Sprawdzenie czy macierz ma same jedynki na przekątnej (jeśli tak to algorytm powinnien zakonczyć działanie)
    if np.count_nonzero(np.diag(A) - 1) != 0:
        for m in range(n+1, A.shape[0]):
            B[m][0] = B[m][0] - B[n][0] * A[m,n]
            A[m,:] = A[m,:] - A[n,:] * A[m,n]
print("Wynik działania Algorytmu eliminacji Gaussa bez pivotingu generującego jedynki naprzekątnej macierzy. \n A={0} \n B={1}".format(A,B))

A = np.random.randint(0, 10, (10, 10)).astype(np.float32)
B = np.random.randint(0, 10, (10, 1)).astype(np.float32)

#Algorytm eliminacji Gaussa bez pivotingu nie generujący jedynekna przekątnej macierzy U
for n in range(0, A.shape[0]):
    for m in range(n+1, A.shape[0]):
        B[m][0] = B[m][0] - B[n][0] * A[m,n] / A[n,n]
        A[m,:] = A[m,:] - A[n,:] * A[m,n] / A[n,n]
        
print("Wynik działania Algorytmu eliminacji Gaussa bez pivotingu nie generującego jedynek naprzekątnej macierzy. \n A={0} \n B={1}".format(A,B))