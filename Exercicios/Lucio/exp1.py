salarios = []
maioresSalarios = []
soma = 0

cont = 1
while cont <= 10 :
    askSalary = float(input("Qual é o salário? R$ "))
    salarios.append(askSalary)
    print(salarios)
    cont += 1

media = sum(salarios)/len(salarios)

for i in range(len(salarios)):
    if(salarios[i] > media):
        maioresSalarios.append(salarios[i])

print(salarios)
print('Salarios acima da média:',maioresSalarios)
