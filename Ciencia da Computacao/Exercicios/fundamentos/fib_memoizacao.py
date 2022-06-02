def fibm(n, memo={1:1, 2:1}):
    if n not in memo: memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

def main():
    for i in range(1, 7 + 1):
        print(fibm(i), end=' ')

main()