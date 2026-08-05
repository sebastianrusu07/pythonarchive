if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    totalSum = sum(numbers)
    appCount = {}
    indexBeforePair = {}  # basically the position from which, when looking to the right, you will see at least 2 of that nr
    reversedPositions = [[] for _ in range(n)]
    for i in range(n-1,0-1,-1):
        appCount[numbers[i]] = appCount.get(numbers[i], 0) + 1
        reversedPositions[numbers[i]].append(i)
        if numbers[i] not in indexBeforePair:
            indexBeforePair[numbers[i]] = -1
        elif indexBeforePair[numbers[i]] == -1:
            indexBeforePair[numbers[i]] = i-1


    queries = []
    for key,appPoint in indexBeforePair.items():
        if appPoint != -1:
            queries.append((appPoint,key))

    queries = sorted(queries)

    moosSoFar = set()
    i = 0
    total = 0

    for key,appPoint in queries:
        while i <= appPoint:
            moosSoFar.add(numbers[i])
            i+=1

        total += len(moosSoFar)
        if key in moosSoFar:
            total -= 1

    print(total)



