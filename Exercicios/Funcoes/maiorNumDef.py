def maiorNum(valor, valor2):
    if(valor > valor2):
        return(f'O valor {valor} é maior.')
    else:
        return(f'O valor {valor2} é maior.')

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
resultado = maiorNum(num1, num2)

print(f'Resultado: {resultado}')