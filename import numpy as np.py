import numpy as np
a = np.array([[1,2],[3,4]])
A =a.std() #standard deviation
print(A)
B = a.sum() #10
print(B)
C = a.mean() #2.5
print(C)
D = a.min() #1
print(D)
E = a.max() #4
print(E)

F = a.sum(axis=0) ## sum of columns
print(F)
G = a.sum(axis=1)#sum of rows
print(G)