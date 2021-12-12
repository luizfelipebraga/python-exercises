def busca_linear(valor, sequencia):
  for item in sequencia:
    print(item)
  if valor == item:
    return True
  return False

def busca_binaria(valor, sequencia):
  inicio = 0
  fim = len(sequencia) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    print(sequencia[meio])
    if valor == sequencia[meio]: return True
    elif valor < sequencia[meio]: inico = meio +1
    else: fim = meio - 1
  return False

lista = [64,55,46,73,37,82,28,91,19]
busca_linear(95,sorted(lista, reverse=False))
print()
busca_binaria(95,sorted(lista, reverse=True))