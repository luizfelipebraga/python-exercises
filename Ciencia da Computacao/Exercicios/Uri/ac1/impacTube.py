qnt = int(input())

canais = [input().split(';') for _ in range(qnt)]
valorFixo = [float(input()) for _ in range(2)]  

print("-----")
print("BÔNUS")
print("-----")

for canal in canais:
    nome = str(canal[0])
    valorBoni = int(canal[1]) // 1000
    if canal[3] == "sim":
        bonificacao = float(canal[2]) + (valorBoni * valorFixo[0])
    else:
        bonificacao = float(canal[2]) + (valorBoni * valorFixo[1])
    
    print(f"{nome}: R$ {bonificacao:.2f}")