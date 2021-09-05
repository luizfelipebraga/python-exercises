n = int(input("Digite a quantidade de numeros: "))
count = 1
t1 = 0
t2 = 1
while count <= n:
    t3 = t1+t2
    print(' -> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    count = count + 1  

print('fim')