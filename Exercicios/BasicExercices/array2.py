allArray = []
parArray = []
imparArray = []

for n in range(20):
    number = int(input("Digite o número: "))
    allArray.append(number)
    if(number%2 == 0):
        parArray.append(number)
    else:
        imparArray.append(number)

print(f'Todos os números: {allArray}')
print(f'Todos os números pares: {parArray}')
print(f'Todos os números imares: {imparArray}')