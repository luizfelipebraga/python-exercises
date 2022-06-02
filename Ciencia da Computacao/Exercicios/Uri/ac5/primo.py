def primo1(n):
  divisores = 0
  for i in range(2, n):
      if n % i == 0:
          divisores += 1
  return divisores == 0


def primo2(n):
  if(n % 2 == 0):
      return n == 2
  for divisor in range(3, n, 2):
    if n % divisor == 0: return False
  return True
