saldoMedio = float(input("Digite seu saldo: R$ "))

if(saldoMedio > 4000):
    saldoMedioAtual = ((saldoMedio*130)/100)
    print(saldoMedioAtual)
elif(saldoMedio > 3000 and saldoMedio <= 4000):
    saldoMedioAtual = ((saldoMedio*125)/100)
    print(saldoMedioAtual)
elif(saldoMedio> 2000 and saldoMedio <=3000):
    saldoMedioAtual = ((saldoMedio*120)/100)
    print(saldoMedioAtual)
else:
    saldoMedioAtual = ((saldoMedio*110)/100)
    print(saldoMedioAtual)