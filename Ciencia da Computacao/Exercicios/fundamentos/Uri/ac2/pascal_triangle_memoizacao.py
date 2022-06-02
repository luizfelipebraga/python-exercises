def pascal_memo(row, column, memo={1:1}):
    if(column == 1 or row == column): return 1
    if(row,column not in memo):
        memo[row, column] = pascal_memo(row-1, column) + pascal_memo(row-1, column-1)
        return memo[row, column]

def main():
    row, column = input().split(' ')

    print(pascal_memo(int(row), int(column)))

main()
