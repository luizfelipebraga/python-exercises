def mist1(a, b):
  a += 20
  b += 50

def mist2():
  a = 30
  b = 60

def mist3():
  global a,b
  a += 40
  b += 70

a = 100
b = 200

mist1(a,b)
print(f'a = {a} | b = {b}') #100 #200

mist2()
print(f'a = {a} | b = {b}')

mist3()
print(f'a = {a} | b = {b}')