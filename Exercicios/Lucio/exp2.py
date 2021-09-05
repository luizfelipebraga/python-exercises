salarios = []
maioresSalarios = []
askSalary = float(input("Qual é o salário? R$ "))

while askSalary >= 0:
    salarios.append(askSalary)
    askSalary = float(input("Qual é o salário? R$ "))

media = sum(salarios)/len(salarios)

for i in salarios:
    if(i > media):
        maioresSalarios.append(i)

print(salarios)
print('Salarios acima da média:',maioresSalarios)