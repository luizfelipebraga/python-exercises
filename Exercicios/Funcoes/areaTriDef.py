def areaTriangulo(baseTri, alturaTri):
    return((baseTri*alturaTri)/2)

base = int(input("Digite a base do triângulo: "))
altura = int(input("Digite a altura do triângulo: "))

resultado = areaTriangulo(base, altura)

print(f'O resultado da área do triângulo é: {resultado:0.0f}cm')