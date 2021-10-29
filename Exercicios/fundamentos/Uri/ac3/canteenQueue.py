# def Queue():
#     students = int(input())

#     index = 1

#     while index <= students:
#         qntGrades = int(input())
#         grades = input().split(' ')

#         if(qntGrades != len(grades)):
#             break

#         for nota in grades:
#             print('nota', nota, end="")

#         index += 1
#     print(grades)


# def main():
#     Queue()

# main()

def VerifyIndex(arr, n):
    for i in range(1, n - 1, 1):
      index = 0
      if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
          print('aa',arr[i])
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
            print('oi')
            break

        print(VerifyIndex(grades, n))

        index = index + 1