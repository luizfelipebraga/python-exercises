# Suponha que você foi contratado para desenvolver uma funcionalidade no sistema
# do RH de um novo banco digital. Esse banco teve acesso ao cadastro de clientes
# de outras três empresas concorrentes (Nubank, C6 e Inter) e gostaria de saber
# quais são os potenciais clientes. Para isso, pediu que você gerasse um relatório
# de acordo com algumas exigências.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6 = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter = set(['duda', 'ilma', 'joão', 'katia', 'luiza', 'fabio'])

#  1) Quais são os clientes de todas as concorrentes.
lista = list(nubank | c6 | inter)
lista.sort()

for cliente in lista: print(cliente)

#  2) Quais são os clientes de cada uma, separadamente.
for cliente in nubank: print('nubank',cliente)
for cliente in c6: print('c6',cliente)
for cliente in inter: print('inter',cliente)

#  3) Quais são os clientes da Nubank que também são clientes do C6.
for cliente in nubank & c6: print('uniao1',cliente)

#  4) Quais são os clientes da Nubank que também são clientes do Inter.
for cliente in nubank & inter: print('uniao2',cliente)

#  5) Quais são os clientes do C6 que também são clientes do Inter.
for cliente in c6 & inter: print('uniao2',cliente)

#  6) Quais são os clientes apenas da Nubank.
for cliente in (nubank - c6 - inter): print('uniao3',cliente)

#  7) Quais são os clientes apenas do C6.
for cliente in (c6 - nubank - inter): print('uniao4',cliente)

#  8) Quais são os clientes apenas do Inter.
for cliente in (inter - c6 - nubank): print('uniao5',cliente)

#  9) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
for cliente in (nubank ^ c6): print('uniao6', cliente)

# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
for cliente in (nubank ^ inter): print('uniao7', cliente)

# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
for cliente in (c6 ^ inter): print('uniao8', cliente)
