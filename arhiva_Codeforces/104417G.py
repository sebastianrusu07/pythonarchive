def selectiveSum(numbers):
    n = len(numbers)
    total = 0
    i = 0
    while i < n-1 and numbers[i]+numbers[i+1] > 0:
        total += numbers[i] + numbers[i+1]
        i+=2
    return total


t = int(input())

for case in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    keyNumbers = [numbers[i]-i for i in range(0,n)]
    groups = {}

    for i in range(n):
        if keyNumbers[i] not in groups:
            groups[keyNumbers[i]] = [numbers[i]]
        else:
            groups[keyNumbers[i]].append(numbers[i])

    totalSum = 0
    for key,item in groups.items():
        totalSum += selectiveSum(sorted(item,reverse=True))

    print(totalSum)