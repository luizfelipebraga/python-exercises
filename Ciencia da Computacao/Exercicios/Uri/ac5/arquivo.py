with open('entrada.txt', 'r') as entrada:
  pares = open('pares.txt', 'r')
  impares = open('impares.txt', 'r')

  for linha in entrada:
    print(type(linha),'aaaaa')
    n = linha
    print(type(n))
    if n % 2 == 0:
      pares.write(f'{n}')
    else: impares.write(f'{n}')

