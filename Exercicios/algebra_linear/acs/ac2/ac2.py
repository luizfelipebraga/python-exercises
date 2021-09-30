import numpy as np 

#1-------ESCALAR-----------------
# a =  [-2, 1, 5, -4, 1]
# b = [3, 4, 2, -3, 0]

# print(np.dot(a, b))

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
# a = np.array([7,6])
#l1 = np.linalg.norm(a,1)
# l1 = LA.norm(a,1)
# print(l1)

# a = np.array([2,3,4])
# l2 = LA.norm(a,2)
# print(l2)
#----------------------------


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