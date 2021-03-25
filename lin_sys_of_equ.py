# This is a program to solve simple Linear Systems of Equations

import numpy as np 

# Equations:
# 1x + 1y = 35
# 2x + 4y = 94

#A = np.matrix([[1,1],[2,4]])
#B = np.matrix([[35],[94]])
A = np.array([[1,2,3],[4,5,6],[1,8,5]])
B = np.array([[4],[7],[1]])

print("Matrix A is: \n",A)
print("Matrix B is: \n",B)

A_inv = np.linalg.inv(A)

print("A_inverse is: \n",A_inv)

X = A_inv.dot(B)

print("The Solution is: \n",X)