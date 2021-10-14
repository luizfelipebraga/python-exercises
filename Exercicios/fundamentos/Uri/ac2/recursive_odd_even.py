def odd_even(n):
    if(n >= 0 | n <= 1000):
        if(n == 0): return True
        elif(n == 1): return False
        else: return odd_even(n-2)
        

def main():
    n = int(input())
    resultado = odd_even(n)
    if(resultado):
        print('numero par')
    else: print('numero nao par')

main()