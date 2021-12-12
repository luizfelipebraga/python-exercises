def gauss_jacobi(a, b, vetorS, iteracoes):
  iteracao = 0
  vetorA = []
  for x in range(len(vetorS)):
    vetorA.append(0)
  while (iteracao < iteracoes):
    for i in range(len(a)):
      x = b[i]
      for j in range(len(a)):
        if i != j:
          x-= a[i][j]*vetorS[j]
      x/=a[i][j]
      vetorA[i]=x
    iteracao +=1

    for k in range(len(vetorA)):
      vetorS[k] = vetorA[k]
  return vetorS

def gauss_seidel(a, b, vetorSolucao, iteracoes):
  iteracao = 0
  while iteracao < iteracoes:
    for i in range(len(a)):
      x = b[i]
      for j in range(len(a)):
        if i != j:
          x -= a[i][j]*vetorSolucao[j]
      x/=a[i][j]
      vetorSolucao[i] = x
    iteracao += 1
  
  return vetorSolucao

def main():
  a = [[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]
  b = [6,25,-11,15]
  vetor = [0,0,0,0]
  n_interacoes = 5
  print('Metodo de Gauss-Jacobi:',gauss_seidel(a,b,vetor,n_interacoes))
  print()
  print('Metodo de Gauss-Seidel:',gauss_seidel(a,b,vetor,n_interacoes))
main()