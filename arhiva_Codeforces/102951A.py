n = int(input())

xCoords = list(map(int,input().split()))
yCoords = list(map(int,input().split()))

bestDist = 0
for i in range(0,n,1):
    for y in range(i+1,n):
        dist = (xCoords[i]-xCoords[y])**2 + (yCoords[i]-yCoords[y])**2
        bestDist = max(bestDist,dist)

print(bestDist)
