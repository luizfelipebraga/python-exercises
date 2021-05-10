nota1 = int(input("Digite a primeria nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

presenca = int(input("Digite a porcetagem de presença: "))

resultado = (nota1+nota2+nota3)/3

if(resultado >= 6 and presenca >= 75):
    print("Aluno aprovado")

elif(resultado > 8):
    print("Aluno aprovado")
    
else:
    print("Aluno reprovado")

