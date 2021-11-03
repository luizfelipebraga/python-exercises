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