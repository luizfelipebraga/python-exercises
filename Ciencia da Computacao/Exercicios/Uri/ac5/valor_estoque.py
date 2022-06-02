produtos = [['notebook', False, 40, 5900.00] , ['tablet',True, 10, 1800.00], ['notebook',True, 35, 1299.00]]

def valor_estoque1(produtos):
  valor = 0
  for produto in produtos:
    valor += produto[1] * produto[2]
  return valor

def valor_estoque2(produtos):
  valor = 0
  for linha in range(len(produtos)):
    valor += produtos[linha][1] * produtos[linha][2]
  return valor

def valor_estoque3(produtos):
  valor = 0
  for linha in range(len(produtos)):
    valor += produtos[1] * produtos[2]
  return valor

print(valor_estoque1(produtos))
print(valor_estoque2(produtos))
print(valor_estoque3(produtos))