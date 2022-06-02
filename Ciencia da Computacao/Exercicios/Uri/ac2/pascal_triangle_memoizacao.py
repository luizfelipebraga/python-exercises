def pascal(row, column):
    if(column == 1 or row == column): return 1
    return pascal(row-1, column) + pascal(row-1, column-1)

def main():
    askTriangle = [input().split(' ')]
    for i in askTriangle:
        row = int (i[0])
        column = int (i[1])

    resultado = pascal(row, column)
    print(resultado)

main()
