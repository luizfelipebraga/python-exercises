a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("O que deseja fazer com os números?\n 1.Média entre os dois números \n 2.Diferença do maior pelo menor\n 3.O produto entre os dois números\n 4.A Divisão do primeiro pelo segundo")

result = int(input(""))

if(result == 1) :
    print((a+b)/2)
elif(result == 2):
    if(a > b):
        print(a-b)
    else :
        print(b-a)
elif(result == 3):
    print(a*b)
elif(result == 4):
    print(a/b)
else: print("Erro")