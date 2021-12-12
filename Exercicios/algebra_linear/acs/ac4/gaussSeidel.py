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
  
  print(vetorSolucao)

gauss_seidel([[2,-1,1],[2,2,2],[-1,-1,2]],[-1,4,-5],[0,0,0,0],25)
gauss_seidel([[2,-1,1],[2,2,2],[-1,-1,2]],[-1,4,-5],[0,0,0,0],25)


