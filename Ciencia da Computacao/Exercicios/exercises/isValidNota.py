import os
from time import sleep

while True:
    nota = int(input("Digite sua nota: "))
    if(nota >= 0 and nota <= 10):
        print("Nota válida")
        break
    else:
        print("Nota inválida")
        sleep(1)
    os.system("cls")


    
    