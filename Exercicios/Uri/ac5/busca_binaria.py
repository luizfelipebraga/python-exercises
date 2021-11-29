def busca_linear(valor, sequencia):
  for item in sequencia:
    print(item)
  if item == valor:
    return True
  return False

def busca_binaria(valor, sequencia):
  inicio = 0
  fim = len(sequencia) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    print(sequencia[meio])
    if valor == sequencia[meio]: return True
    elif valor < sequencia[meio]: fim = meio -1
    else: inicio = meio + 1
  return False

lista = [19,28,37,46,55,64,73,82,91]
busca_linear(95,lista)
print()
busca_binaria(95,lista)