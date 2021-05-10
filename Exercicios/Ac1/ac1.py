#Exercicio1
# salariofix = float(input("Digite o sálario fixo do funcionário: R$ "))
# vendas = int(input("Digite o valor de vendas do funcionário: R$ "))

# salarioFinal = salariofix + ((vendas * 4)/100)

# print(f"O salário final do funcionário é: R$ {salarioFinal:.2f}")



# Exercicio2
# dimensao1 = int(input("Valor da dimensão 1: "))
# dimensao2 = int(input("Valor da dimensão 2: "))

# totalDimensao = dimensao1 * dimensao2
# print(f"O total da área é: {totalDimensao} m2")

# potenciaIlumi = totalDimensao * 18
# print(f"o total de potência gasta será: {potenciaIlumi}W")


#Exercicio3
# soma1 = int(input("Digite a media do 1º ângulo: "))
# soma2 = int(input("Digite a media do 2º ângulo: "))

# soma3 = 180 - (soma1 + soma2)

# print(f"A medida do terceiro ângulo é : {soma3}º")



#Exercicio4
# print("Tipo - Descrição - Rendimento\n 1 - Poupança - 3%\n 2 - Fundo de Renda Fixa - 4% ")

# tipoInv = int(input("Qual é o tipo de investimento? "))
# valor = int(input("Qual é o valor de investimento: R$ "))

# if(tipoInv == 1):
#     valorFinal = valor + (valor*0.03)
#     print(f"O rendimento será de {valorFinal:.2f}")
# else:
#     valorFinal = valor + (valor*0.04)
#     print(f"O rendimento será de {valorFinal:.2f}")


#Exercicio5
# preco = int(input("Digite o preço do produto: R$ "))

# if(preco <= 30):
#     desconto = 0
# elif((preco > 30) and (preco <= 100)):
#     desconto = preco*0.10
# else :
#     desconto = preco*0.15

# precoFinal = preco - desconto
    
# print(f"Preço atual R${preco} -  {desconto}% de desconto = Preço final com desconto: R$ {precoFinal:.2f}\n ")


#Exercicio6
# senha = 4531

# isSenhaValid = int(input("Digite a senha: "))

# while(isSenhaValid != senha) :
#     print("Acesso negado.")
#     isSenhaValid = int(input("Digite a senha: "))

# print("Acesso permitido.")
