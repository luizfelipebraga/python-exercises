from time import perf_counter

def pares(n):
  saida = open('saida.txt', 'w')
  for i in range(0, n+1, 2): 
    print(i)
    saida.write(f'{i}')
  saida.close()

def impares(n):
  saida = open('saida.txt', 'w')
  for i in range(1, n+1, 2):
    print(i)
    saida.write(f'{i}')
  saida.close()

def primos(n):
  arr = []
  for i in range(1, n+1):
    index = 0
    for j in range(1, i+1):
      if(i % j == 0):
          index += 1
    if(index <= 2):
        arr.append(i)
        
  saida = open('saida.txt', 'w')
  for i in arr:
    print(i)
    saida.write(f'{i}')
  saida.close()
    
def main():
  entrada = open('entrada.txt', 'w')
  ask = input().split(' ')
  entrada.close()
  user_choose = ask[0]
  user_number = int(ask[1])

  if(user_choose == 'primos'):
    inicio_prim = perf_counter()
    primos(user_number)
    termino_prim = perf_counter()
    print('Tempo = ', termino_prim - inicio_prim, 'segundos')

    saida = open('saida.txt', 'w')
    saida.write(f'Tempo = {termino_prim - inicio_prim} segundos')
    saida.close()

  elif(user_choose == 'pares'):
    inici_par = perf_counter()
    pares(user_number)
    termino_par = perf_counter()
    print('Tempo = ', termino_par - inici_par, 'segundos')

    saida = open('saida.txt', 'w')
    saida.write(f'Tempo = {termino_par - inici_par} segundos')
    saida.close()

  elif(user_choose == 'impares'):

    inicio_imp = perf_counter()
    impares(user_number)
    termino_imp = perf_counter()
    print('Tempo = ', termino_imp - inicio_imp, 'segundos')

    saida = open('saida.txt', 'w')
    saida.write(f'Tempo = {termino_imp - inicio_imp} segundos')
    saida.close()
  
  else: print('Tente Novamente')

main()