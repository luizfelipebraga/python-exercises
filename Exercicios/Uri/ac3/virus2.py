from functools import reduce
import operator

def VerifyLethality(arr):
  ages =  arr.copy()

  ages = sorted(ages, reverse=True)
  
  slicePar = ages[0::2]
  sliceImp = ages[1::2]

  nI = len(sliceImp)

  xdifPar = reduce(operator.__sub__, slicePar)
  xdifImpar = reduce(operator.__sub__, sliceImp)

  if 0 in slicePar:
    xdifPar = max(slicePar)
  
  if 0 in sliceImp:
    xdifImpar = max(sliceImp)

  if(nI % 2) != 0:
    xdifImpar = 0

  finalResult = xdifPar + xdifImpar

  return finalResult
  
def main():
    numberVirus = int(input())
    virusAges = [int(x) for x in input().split(' ')]
    print(VerifyLethality(virusAges))
    
while True:
    try:
        main()
    except:
        break