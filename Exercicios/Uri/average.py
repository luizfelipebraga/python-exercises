a = float(input())
b = float(input())

aF = float("{:.1f}".format(a))
bF = float("{:.1f}".format(b))

print(aF)

media = (aF + bF)/2

print(f'MEDIA = {media:.5f}')
