## Without Memoizacao -----------------------------
import math

def combination(row, column):
    return int((math.factorial(row)) / ((math.factorial(column)) * math.factorial(row - column)))

def pascal_triangle(row, column, memo={}):
    if(column == 1 or row == column): return 1
    if(row, column not in memo): 
        memo[row, column] = pascal_triangle(row-1, column) + pascal_triangle(row-1, column-1)
        return memo[row, column]

def main():
    L, C = input().split(' ')

    print(pascal_triangle(int(L), int(C)))

main()

# if(row >= 1 and row <= 800 and column >= 1 and column <= 800):
    #     resultado = pascal_triangle(row, column)
    #     print(resultado)
    # else: print('Numero incorreto')

##--------------Finished-------------------------

# MEMOIZACAO---------------------------------


#--------------------------------------------