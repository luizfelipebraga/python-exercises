produtos = [['smartphone', 100, 1199.00] , ['televisao', 5, 2599.00], ['notebook', 20, 4500.00]]

def valor_estoque(produtos):
  valor = 0
  for produto in produtos:
    valor += produto[1] + produto[2]
  return valor

def valor_estoque(produtos):
  valor = 0
  for linha in range(len(produtos)):
    valor += produtos[linha][1] * produtos[linha][2]
  return valor

def valor_estoque(produtos):
  valor = 0
  for linha in range(len(produtos)):
    valor += produtos[1] * produtos[2]
  return valor