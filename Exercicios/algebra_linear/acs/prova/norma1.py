# Nome: Luiz Felipe Braga Alves de Souza

from numpy import linalg as LA
import numpy as np

#A)
u = np.array([2,-2,1,3,0])
A= np.linalg.norm(u,1)
A= LA.norm(u,1)
print(A)

#B)
v = np.array([1,1,-1,0,2])
dist = np.linalg.norm(u-v)

print(dist)
