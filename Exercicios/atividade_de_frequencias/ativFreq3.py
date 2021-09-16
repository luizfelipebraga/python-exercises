# import random 

# arrayA =  [random.randint(0, 50) for x in range(5)]
# arrayB = [random.randint(0, 50) for x in range(5)]
# arrayC = []
# i = 0
# arrayB.reverse()

# while i < len(arrayA):
#     arrayC.append(arrayA[i] - arrayB[i])
#     i+=1
# print(arrayC)


# arrayA = []
# arrayPrimo = []
# for x in range(2,20):
#     arrayA.append(x)

# for i in arrayA:
#     index = 0
#     for j in range (1, i+1):

##       loop 2%1 2%2 2%3...
#         if(i % j == 0):
#             index += 1

#     if(index <= 2):
#         print(index)
#         arrayPrimo.append(i)
# print(arrayPrimo)


# arrayA = [random.randint(1, 20) for x in range(15)]
# arrayB = []

# i = 0
# Vmax = max(arrayA)

# while i < len(arrayA):
#     arrayB.append(Vmax % arrayA[i])
#     i+=1

# print(arrayB)