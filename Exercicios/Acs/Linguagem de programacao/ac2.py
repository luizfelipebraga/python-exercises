#1
# cod = int(input("Digite o código: "))
# if (cod != 1234):
#     print("Código inválido")
# else:
#     senhaUser = int(input("Digite a senha: "))
#     senha = 9999
#     n = 0

#     if(senhaUser != senha):
#         while n <=3 :
#             print("senha incorreta")
#             n=n+1
#             senhaUser = int(input("Digite a senha:"))
#             if(n == 3):
#                 print("Senha bloqueada contate o administrador")
#                 break
#     else:
#         print("Acesso Permitido")


#2
# pessoa = 1
# idade15 = 0
# idade20 = 0
# idade40 = 0
# idade45 = 0
# while pessoa < 9:
#     inputIdade = int(input("Digite a idade: "))
#     pessoa = pessoa + 1
#     if(inputIdade <= 15):
#         idade15 = idade15 + 1
#     elif(inputIdade >15 and inputIdade <=30):
#         idade20 = idade20 + 1
#     elif(inputIdade> 30 and inputIdade <= 45):
#         idade40 = idade40 + 1
#     else:
#         idade45 = idade45 + 1

# print("Até 15 anos:",idade15)
# print("De 15 a 30 anos:",idade20)
# print("De 30 a 45 anos:",idade40)
# print("Acima de 45:",idade45)


#3
# quantVista = 0
# vista = 0
# quantPrazo = 0
# prazo = 0
# transaction = 0
# while transaction < 16:
#     codigo = input("Digite o código: ")
#     valor = float(input("Digite o valor: R$ "))
#     transaction = transaction + 1
#     if(codigo.lower() == 'v'):
#         vista = vista + valor
#         quantVista = quantVista + 1
#     elif(codigo.lower() == 'p'):
#         prazo = prazo + valor
#         quantPrazo = quantPrazo + 1
#     else:
#         print("Código não encontrado")

# print(f'{vista:0.2f}')
# print(f'{prazo:0.2f}')
# print(quantVista + quantPrazo)


#4 
# def soma(n1, n2):
#     for i in range(n1, n2):
#         return i + n1 + n2

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o primeiro número: "))
# resultado = soma(num1, num2)
# print("Resultado:", resultado)

#5
def valorPagamento(valor, dia):
    if(dia != 0):
        return valor + ((valor*3/100) + (dia*0.1))
    else:
        return valor

quantiPres = 0
valorPres = 0
numPrestacao = 1
while numPrestacao != 0:
    prestacao = int(input("Digite o valor da prestação: R$ "))
    if(prestacao == 0):
        break
    numeroDias = int(input("Digite o número de dias atrasados: "))
    quantiPres = quantiPres + 1
    valorPres = valorPres + prestacao
    resultado = valorPagamento(prestacao, numeroDias)
    print(resultado)
print(f"Relatório do dia: quantidade de prestações: {quantiPres}, total valor: {valorPres:0.2f}")




