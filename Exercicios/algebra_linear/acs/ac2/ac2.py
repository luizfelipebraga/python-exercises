import numpy as np 

#1-------ESCALAR-----------------
# a =  [1, 1, -1, 1, 1]
# b = [-2, 3, -2, 3, -2]

# print(np.dot(a, b))

#----------angulo
vector_1 = [1, -1, 1, -1, 1]
vector_2 = [1, 1, 1, 1, 1]

unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
dot_product = np.dot(unit_vector_1, unit_vector_2)
angle = np.arccos(dot_product)

print(angle)

#2------------------
# a = [1,1,1]
# b = [2,1,-3]
# c = 3^[1,1,1]
# print(c)

# resultado = c + b
# print(resultado)
#--------------------

#-------------------------------------
###(x² + 2x - 35) (x² - 8x - 48) = 0 
# 4 + 140 = 144
# raiz = 7

# -2 + 12/2 = 5
# -2 -12/2 = -7

# [5,-5] = 10
# [-3, -6] = 9
# [4, 5] = 9
# [-7, 0] = 7
# [2, 3, 4] = 9
#-------------------------------------

#-------------NORMA---------------
from numpy import linalg as LA
u = np.array([2,-2,1,3,0])
l1 = np.linalg.norm(u,1)
l1 = LA.norm(u,1)
print(l1)

# v = np.array([1,1,-1,0,2])
# l2 = np.linalg.norm(v,1)
# l2 = LA.norm(v,2)
# print(l2)
# ----------------------------


#-------SE O RESULTADO DA ESCALAR == 0 OS VETORES SAO PERPENDICULARES-----------
#[10, 0, 5, -6]
#[2, 1, 3, -1]
#[4, 4, 2, -3]
#[7, -7, -5, 6]
#[5, 5, 5, 2]

# u = np.array([3,-3,-2,5])
# v = np.array([5, 5, 5, 2])
# resultado = u.dot(v)
# print(resultado)
#------------------