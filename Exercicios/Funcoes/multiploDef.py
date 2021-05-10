def multiplo(valor, valor2):
    if(valor % valor2 == 0):
        return(True)
    else:
        return(False)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))

resultado = multiplo(num1, num2)

print(f'O resultado é: {resultado}')


