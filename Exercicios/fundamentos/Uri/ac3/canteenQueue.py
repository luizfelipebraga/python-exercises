def VerifyIndex(arr, n):
    a = arr
    b = sorted(a, reverse=True)

    index = 0

    for i in range(n):
        if (a[i] == b[i]):
            index = index + 1
    return index


if __name__ == '__main__':
    students = int(input())
    index = 1

    while index <= students:
        qntGrades = int(input())
        grades = [int(x) for x in input().split(' ')]
        n = len(grades)

        if(qntGrades != n):
            break

        print(VerifyIndex(grades, n))

        index = index + 1

# n = int(input())
# while n > 0:
#     n -= 1
#     m = int(input())
#     a = input().split()
#     for ind, i in enumerate(a):
#         a[ind] = int(a[ind])
#     b = sorted(a)
#     b.reverse()
#     total = 0
#     for ind, i in enumerate(a):
#         if (a[ind] == b[ind]):
#             total +=1
#     print(total)
