def main():
    count = 1

    queries = []
    grades = []

    ask = [int(x) for x in input().split(' ')]


    numCitizens = ask[0]
    numQueries = ask[1]

    while count <= numCitizens:
        if(count < 1 and count > 100):
          break
        grades.append(int(input()))
        count += 1

    sortedGrades = sorted(grades, reverse=True)
    
    count = 1

    while count <= numQueries:
        if(count < 1 and count > 100):
          break
        position = int(input())
        queries.append(sortedGrades[position - 1])
        count += 1

    for i in queries:
        print(i)

main()