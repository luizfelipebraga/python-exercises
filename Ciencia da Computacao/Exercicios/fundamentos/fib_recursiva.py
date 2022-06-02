def fib(n):
    if (n<=2): return 1
    else: return fib(n-1) + fib(n-2)

def main():
    for i in range(1, 5 + 1):
        print(fib(i), end=" ")

main()