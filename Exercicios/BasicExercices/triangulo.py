lado1 = int(input("digite o tamanho para do lado 1: "))
lado2 = int(input("digite o tamanho para do lado 2: "))
lado3 = int(input("digite o tamanho para do lado 3: "))

equi = "Equilátero"
iso = "Isó"
esca = "Escaleno"

if lado1 == lado2 and lado2 == lado3:
        print(f"triangulo {equi}")

elif lado1 != lado2 or lado2 != lado3:
        print(f"triangulo {esca}")
else:
    print(f"triangulo {iso}")
    