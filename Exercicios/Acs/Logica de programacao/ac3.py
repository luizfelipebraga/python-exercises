# def misterio (x, v, n):
#     i = 0
#     while i< n and v[i] != x:
#         i = i+1

#     if(i< n):
#         return i
#     else:
#         return -1

# a = ['b', 'x', 'd', 'v', 'e', 'r', 'e', 'p']

# r1 = misterio('e', a , 8)
# r2 = misterio('z', a , 8)
# r3 = misterio('v', a , 3)
# print(r1)
# print(r2)
# print(r3)
# saida 4 -1 -1



# def enigma(v, n) :
#     i=0
#     while(i<n):
#         v[i] = 2*v[i]
#         i = i+2
#     return

# def exibe(v, n):
#     i=0
#     while(i<n):
#         print(v[i], end='')
#         i = i+1
#     return
    
# v = [10, 20, 30, 40, 50]
 
# enigma(v, len(v))
# exibe(v, len(v))

# print(v)
#exibe 20, 20, 60, 40, 100




# def bubble_sort(v, n):
#     exibe(v, n)

#     tam = n

#     while tam > 1:
#         empurra(v, tam)
#         exibe(v, tam)
#         tam = tam - 1

#     exibe(v, n)
#     return 

# def empurra(v, n):
#     i = 0
#     while (i < n-1):
#         while(v[i] > v[i+1]):
#             troca(v, i, i+1)
#         i = i+1
#     return

# def troca(v, i, j):
#     temp = v[i]
#     v[i] = v[j]
#     v[j] = temp
#     return

# def exibe(v, n):
#     i = 0
#     while (i < n):
#         print(v[i], end='')
#         i = i+1
#     print('\n')
#     return

# bubble = [40,20,50,30,10]
# bubble_sort(bubble, len(bubble))



# def mediap(vet, n):
#     s = 0
#     cp = 0
#     pos = 0

#     while (pos < n):
#         if(vet[pos] % 2 == 0):
#             cp += 1
#             s += vet[pos]
#         pos += 1
    
#     print(s)
#     print(cp)
#     print(pos)
#     print(s/cp)
#     return s/cp

# exampleArray = [1,2,3,4,5,6,7,8,9,10]
# mediap(exampleArray, len(exampleArray))



# idades = [9,8,6,10,7,3,2]
# pos = 0
# while pos < 7:
#     print('Valor das posicoes', pos, '=', idades[pos])
#     pos += 1

