import random

codProdClient = []
codProd = []
totalProd = [random.randint(10, 300) for p in range(1, 11)]

for x in range(1,11):
    codProdClient.append(x)
    codProd.append(x)

while True:
    client = int(input("Digite o número do client: "))
    print(codProdClient)
    if(client == 0 and client != codProdClient):
        break

    cod = int(input("Digite o código do produto: "))
    if(cod == codProd):
        askAmount = int(input("Digite a quantidade: "))
        if(totalProd[cod] <= askAmount):
            print('Estoque insuficiente')
            break
        totalProd[cod] = totalProd[cod] - askAmount
        print(totalProd)
    else:
        print('Código inválido')

        
        #cod = 0
        #codProd = [1,2,3,4,5,6,7,8,9,10]
        ##if(cod == codProd)
        ##verifica se o valor cod existe no codProd
        
        #false

         
        #cod = 0
        #codProd = [1,2,3,4,5,6,7,8,9,10]
        ##if(cod in codProd)
        ##verifica se a posicao cod existe no codProd

        #true


