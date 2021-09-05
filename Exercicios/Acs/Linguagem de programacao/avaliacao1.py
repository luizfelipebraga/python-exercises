###1
# i = 0
# numArray = []
# while i < 10:
#     askNum = int(input("Digite um numero: "))
#     numArray.append(askNum)
#     i+=1

# numArray.sort()
# print(numArray)


##2
# askValue = int(input("Digite o valor da casa: "))
# askSalary = int(input("Digite o salario mensal: "))
# menorSalary = (askSalary*30)/100
# askYear = int(input("Digite o total de anos a pagar: "))

# valorPrest = askValue / (askYear*12)

# if(valorPrest > menorSalary):
#     print("Empréstimo negado")

# else:
#     print('Empréstimo aprovado')



##3
# arrayA = []
# arrayB = []

# def readNum(numero):
#     arrayA.append(numero)
#     arrayB.append(numero)

    
# while True:
#     numero = int(input("Digite um número: "))
#     if(numero == 0):
#         break
#     readNum(numero)

# VmaxA = max(arrayA)
# somaA = sum(arrayA)
# lenA = len(arrayA)

# mediaA = somaA / lenA
# print('Media A: ',mediaA,'Max:',VmaxA)

# VmaxB = max(arrayB)
# lenB = len(arrayB)
# somaB = sum(arrayB)

# mediaB = somaB / lenB
# print('Media B: ',mediaB,'Max:',VmaxB)

##4
# codigo = input("Digite o codigo do empregado: ")

# anoNasciment = int(input("Digite o ano de nascimento: "))
# idade = 2020 - anoNasciment

# anoIngresso = int(input("Digite o ano de ingresso na empresa: "))
# minJob = 2021 - anoIngresso

# print('idade do empregado: ',idade, 'e o ano de ingresso na empresa:',minJob)

# anwser = input("Requerer aposentadoria ou Não querer? ")

# if(anwser.lower() == 's' or anwser == 'sim'):
#     if((idade >= 63) or (minJob >= 30) or (idade >= 63 and minJob >= 25)):
#         print('Aposentadoria aprovada.')
#     else:
#         print('Aposentadoria recusada.')


##5
# arrayNum = []
# for i in range(30,80+1):
#     arrayNum.append(i)


# sumArray = sum(arrayNum)
# lenArray = len(arrayNum)
# media = sumArray / lenArray

# print(media)