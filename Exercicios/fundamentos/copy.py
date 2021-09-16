from copy import copy

original = [10, 20, 30, 40, 50]

copia1 = original            # cópia da referência à lista
copia2 = original[:]         # cópia rasa da lista
copia3 = original.copy()     # cópia rasa da lista
copia4 = copy.copy(original) # cópia rasa da lista
copia5 = list(original)      # cópia rasa da lista

print(original)
print(copia5)

copia5[0] = 77

print(original)
print(copia5)