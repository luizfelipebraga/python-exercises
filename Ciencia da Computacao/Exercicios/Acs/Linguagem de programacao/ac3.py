# 16.
# media = 0
# value1 = 0
# media1 = 1

# names = []

# for x in range(5):
#     nome = input("Digite o nome do produto: ")
#     valor = int(input("Digite o valor do produto: "))

#     if(valor < 50):
#         value1 = value1 + 1
    
#     elif(valor >= 50 and valor <= 100):
#         names.append(nome)

#     elif(valor >= 100):
#         media = valor/media1
#         media1 = media1 + 1

# print(value1)
# print(names)
# print(media)


#17
# vetor1 = [31,392,1,40,5,6,7,8,9,10]
# vetor2 = [11,1232,232,234,15,16,17,18,19,20]
# vetor3 = vetor1 + vetor2
# vetor3.sort(key=int, reverse=True)
# print(vetor3)


#18
# vetor1 = [2,323,23,23,3,424,234,234,234,2,34,23,4,65,76]
# vMax = (max(vetor1))
# vMin = (min(vetor1))

# print(f'O maior elemento: {vMax} e a posição no array: {vetor1.index(vMax)}')
# print(f'O menor elemento: {vMin} e a posição no array: {vetor1.index(vMin)}')

#19
# vetor1 = [31,392,1,40,5,6,7,8,9,10]
# vetor2 = [11,1232,232,234,15,16,17,18,19,20]

# numeros = 0
# vetor3 = []

# while numeros < len(vetor1):
#     vetor3.append(vetor1[numeros] * vetor2[numeros])
#     numeros = numeros + 1

# print(vetor3)


#20
# import random
# array = [random.randint(-50, 50) for x in range(50)]
# arrayPositivo = []

# for x in range(len(array)):
#     if(array[x] > 0):
#         arrayPositivo.append(array[x])
# arrayPositivo.sort()
# print(arrayPositivo)