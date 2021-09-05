corridas = []

corrida = int(input())

while corrida > 0:
    corridas.append(corrida)
    corrida = int(input())

media = sum(corridas)/len(corridas)
print(f'MEDIA: {media:.2f}')

for x in corridas:
    if(x < media):
        print(x)


