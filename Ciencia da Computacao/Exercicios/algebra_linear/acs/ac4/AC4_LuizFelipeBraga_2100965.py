import numpy as np

A = np.array([[1,-3,2],
              [-2,8,-1],
              [4,-6,5]])

b = np.array([11, -15, 29])

x = np.linalg.solve(A, b)
print(x)




## Exercicios

#1
# [2x1 - x2 + x3 = -1]
# [2x1 + 2x2 + 2x3 = 4]
# [-X1 - X2 + 2X3 = -5]  #solucao (1,2,-1)^t

# #a) método de Jaocb com x^(0) = 0 falha em dar boa aproximacao apos 25 iteracoes
# #b) metodo de gauss-seidel com x^(0) = 0 com precisao de 10^-5 na norma infinito



# #2 Encontrar 2 primeiras iteracoes dos sistemas abaixo para os metodos de jaboc e gauss-seidel, fazendo na mao.
# #Depois exceutar o programa com precisao de 10^-3 e x^(0) = 0

# [3x1 - x2 + x3 = 1]
# [3x1 + 6x2 + 2x3 = 0]
# [3x1 + 3x2 + 7x3 = 4]

# [-2x1 + x2 + 1x3/2 = 4]
# [x1 - 2x2 - 1x3/2 = -4]
# [x2 + 2x3 = 0]


