print(" A – Álcool 1,7997\n D – Diesel 0,9798\n G – Gasolina 2,1009")

choiceFuel = input("Qual combustivel deseja abastecer?: ")
choiceQnt = int(input("Quantos litros: "))

if(choiceFuel.lower() == 'a'):
    resultado = (1.7997*choiceQnt)
    print(resultado)
elif(choiceFuel.lower() == 'd'):
    resultado = (0.9798*choiceQnt)
    print(resultado)
elif(choiceFuel.lower() == 'g'):
    resultado = (2.1009*choiceQnt)
    print(resultado)
else:
    print("Letra errada")


