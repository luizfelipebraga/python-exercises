arrayteste = []

for k in range(18644 , 34088 ):
    if '2' in str(k) and '7' not in str(k):
        print(k)
        arrayteste.append(k)

print(len(arrayteste))