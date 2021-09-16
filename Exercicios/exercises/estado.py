preco = float(input(f"Digite o preco do carro: R$ "))
anoCarro = int(input("Digite o ano do carro: "))

if(anoCarro >= 2010) :
    taxa = ((preco * 3.5)/100)
    print(f"Taxa a pagar: {taxa}")
else : 
    taxa = ((preco * 2.5)/100)
    print(f"Taxa a pagar: {taxa}")