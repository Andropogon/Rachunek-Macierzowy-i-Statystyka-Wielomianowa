# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:39:00 2021

@author: Andro
"""

import numpy as np
import time

matrix_size=100

matrix1 = np.random.randint(0, 10, (matrix_size, matrix_size))
matrix2 = np.random.randint(0, 10, (matrix_size, matrix_size))

print("Program run for matrix size " + str(matrix_size))
#ijk
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix1)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("ijk - operation time -  " + str((end - start)*1000) + "ms")

#ikj
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for i in range(len(matrix1)):
    for k in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("ikj - operation time -  " + str((end - start)*1000) + "ms")

#jik
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for j in range(len(matrix2[0])):
    for i in range(len(matrix1)):
        for k in range(len(matrix2)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("jik - operation time -  " + str((end - start)*1000) + "ms")

#jki
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for j in range(len(matrix2[0])):
    for k in range(len(matrix2)):
        for i in range(len(matrix1)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("jki - operation time -  " + str((end - start)*1000) + "ms")

#kij
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for k in range(len(matrix2)):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("kij - operation time -  " + str((end - start)*1000) + "ms")

#kji
res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
for k in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        for i in range(len(matrix1)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
end = time.time()
print("kji - operation time -  " + str((end - start)*1000) + "ms")
 

res = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
start = time.time()
res = matrix1 @ matrix2
end = time.time()
print("np.dot - operation time -  " + str((end - start)*1000) + "ms")