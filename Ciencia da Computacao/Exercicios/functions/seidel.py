Python 3.9.5 (default, May 11 2021, 08:20:37) 
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def gauss_seidel(a, b, vetorSolucao, iteracoes):
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


