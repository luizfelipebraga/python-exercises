def isValueP(valor):
    if(valor > 0):
        return('P')
    else:
        return('N')

num = int(input('Digite um valor: '))
resultado = isValueP(num)
print('Resultado', resultado)   