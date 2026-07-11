n = int(input())

biggestMedian = 0
previousTime = 0
previousSpeed = 0

for i in range(n):
    a, b = map(int, input().split())

    if i != 0:
        time = a - previousTime
        speed = b - previousSpeed

        biggestMedian = max(biggestMedian, speed // time)

    previousTime = a
    previousSpeed = b

print(biggestMedian)