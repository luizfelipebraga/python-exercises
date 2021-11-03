def FindIndex(arr, num):
    sortedNames = sorted(arr)
    foundIndex = sortedNames[num-1]

    return foundIndex


def main():
    ask = [int(x) for x in input().split(' ')]

    students = ask[0]
    studentNumber = ask[1]

    
    names = []
    counter = 1
    
    while counter <= students:
        
        names.append(input())
        counter+=1
    
    print(FindIndex(names, studentNumber))
        
    
main()