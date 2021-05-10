num = int(input("Digite um número: "))

if((num % 3 == 0) and (num % 5 == 0)) :
    print(f'O número {num} é divisivel por 5 e 3')
else : 
    print(f'O número {num} não é divisivel por 5 e 3')