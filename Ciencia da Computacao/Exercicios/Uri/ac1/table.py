num = int(input())

if(num >= 0 or num <= 10):
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')