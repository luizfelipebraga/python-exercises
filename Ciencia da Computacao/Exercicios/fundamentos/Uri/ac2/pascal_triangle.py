## Without Memoizacao -----------------------------
import math

def combination(column, row):
    return int((math.factorial(column)) / ((math.factorial(row)) * math.factorial(column - row)))

def pascal_triangle(row, column):
    if(column == 1 or row == column): return 1
    
    result = []
    for x in range(row): 
        row = []
        for y in range(x + 1): 
            row.append(combination(x, y))
        result.append(row)

    ## preciso pegar o tamanho para depois pegar o ultimo indice do array pai 
    lenghtDadArray = len(result) - 1
    lastIndexArray = result[lenghtDadArray]

    ## depois de pgar o ultimo indice preciso pegar o tamanho do array filho, e depois pegar o ultimo indice do array - column
    lenghtChildArray = len(lastIndexArray) - column
    lastChildIndex = lastIndexArray[lenghtChildArray]

    return lastChildIndex


def main():
    row, column = input().split(' ')

    print(pascal_triangle(int(row), int(column)))

main()

# if(row >= 1 and row <= 800 and column >= 1 and column <= 800):
    #     resultado = pascal_triangle(row, column)
    #     print(resultado)
    # else: print('Numero incorreto')

##--------------Finished-------------------------

# MEMOIZACAO---------------------------------


#--------------------------------------------