def areaQuadrado(lado):
    return(lado*lado)

lado = int(input("Digite o lado do quadrado: "))
resultado = areaQuadrado(lado)

print(f'A área do quadrado é: {resultado}')