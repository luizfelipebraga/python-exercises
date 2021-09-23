def recusive(n):
    if(n == 0): 
        return 1

    else: 
        return n * recusive(n-1)

def main():
    recusive(5)

main()