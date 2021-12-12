import numpy as np
from numpy import linalg as LA

A = np.array([[1, 2, 3], 
            [4,5,6], 
            [7,8,9]])

autovalores, autovetores = LA.eig(A)

# B = autovalores[0]
B = A.dot(autovetores[:,0])

C = autovetores[:,0]*autovalores[0]
print("Lista de autovalores: \n", autovalores)
print('')
print("Lista de autovetores: \n", autovetores)
print('')
print(B)
print('')
print(C)
