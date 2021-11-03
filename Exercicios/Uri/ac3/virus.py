from functools import reduce
import operator

def VerifyLethality(arr, n):
  ages =  arr.copy()

  slicePar = ages[0::2]
  sliceImp = ages[1::2]

  sortedPar = sorted(slicePar, reverse=True)
  sortedImpar = sorted(sliceImp, reverse=True)

  xdifPar = reduce(operator.__sub__, sortedPar)
  xdifImpar = reduce(operator.__sub__, sortedImpar)

  if 0 in sortedPar:
    xdifPar = 0
  
  if 0 in sortedImpar:
    xdifImpar = 0

  finalResult = xdifPar + xdifImpar

  return finalResult

if __name__ == "__main__":
  numberVirus = int(input())
  virusAges = [int(x) for x in input().split(' ')]
  print(len(virusAges))

  n = len(virusAges)
  print(VerifyLethality(virusAges, n))