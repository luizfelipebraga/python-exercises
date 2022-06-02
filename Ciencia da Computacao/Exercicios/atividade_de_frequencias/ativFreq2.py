#Faça um Programa que solicite ao usuário números e os armazene em uma lista de 30 posições.
#Crie uma função que recebe a lista preenchido e substitua todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0
# def lista(numArray):
#     for x in range(len(numArray)):
#         if(numArray[x] > 0):
#             numArray[x] = 1
#         else:
#             numArray[x] = 0
#     return numArray

# arrayNum = []
# for x in range(30):
#     num = int(input("Digite um número:"))
#     arrayNum.append(num)
#     resultado = lista(arrayNum)

# print(arrayNum)


#2 Crie uma função que leia um número indeterminado de valores inteiros, armazene em duas listas (A e B)
#e encerre a entrada de cada lista quando o usuário informar um valor igual a -1 que não deve ser armazenado). 
# Exiba ao usuário o valor máximo e mínimo das duas listas

# arrayA = []
# arrayB = []
# while True:
#     num = int(input("Digite um número: "))
#     if(num == -1):
#         break
#     arrayA.append(num)
#     arrayB.append(num)

# print(min(arrayA))
# print(max(arrayA))

# print(min(arrayB))
# print(max(arrayB))


#3 Faça uma Função que leia uma lista com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos dessa lista.
# def somaArray(arrayNum):
#     soma = 0
#     for x in range(len(arrayNum)):
#         soma = soma + (arrayNum[len(arrayNum)-1]**2)
#     return print("A soma dos quadrados do elemento é igual:", soma)

# arrayNum = []
# for x in range(10):
#     arrayNum.append(int(input("Digite um número: ")))
# resultado = somaArray(arrayNum)


#4Faça uma Função que leia duas listas com 10 números inteiros e gere uma terceira lista com 20 elementos e mostre o resultado em tela. 
#OBS: os valores dessa terceira lista deverão ser compostos pelos elementos intercalados das duas listas anteriores. Por exemplo:
#  lista1: [1,2,3,4...] lista2:[20,21,22...] lista3:[1,20,2,21,3,22,4...]
# arrayA = []
# arrayB = []
# arrayC = []
# num = 1
# while num < 5:
#     num = int(input("Digite um numero: "))
#     arrayA.append(num)
#     arrayC.append(num)
#     numb = int(input("Digite um número b: "))
#     arrayB.append(numb)
#     arrayC.append(numb)
#     num = num + 1

# print(arrayA)
# print(arrayB)
# print(arrayC)