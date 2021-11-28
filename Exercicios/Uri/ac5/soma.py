def soma(lista, tamanho):
  if tamanho == 0: return 0
  return lista[tamanho-1] + soma(lista, tamanho-1)

L = [10, 20, 30, 40, 50]
print(f'soma(L,5) = {soma(L, 5)}')