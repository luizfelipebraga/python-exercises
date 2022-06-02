def main():
    numChildren = int(input())

    arrName = []
    aprov = []
    reprov = []
    counter = 1

    while counter <= numChildren:
        children = input()

        status, names = children.split(' ')

        if(status == '-'):
            reprov.append(status)
            arrName.append(names)
        else: 
            aprov.append(status)
            arrName.append(names)

        counter = counter + 1
        
    sortedNames = sorted(arrName)
    a = len(aprov)
    r = len(reprov)

    for i in sortedNames:
        print(i)
    print(f'Se comportaram: {a} | Nao se comportaram: {r}')


main()