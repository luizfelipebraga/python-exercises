array = []
for i in range(10):
    x = int(input())
    if(x <= 0):
        x = 1
    array.append(x)
    print(array)

for i in range(len(array)):
    print(f"X[{i}] =", array[i])