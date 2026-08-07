import sys

def distToPoint(cow,point):
    if cow[0] == "E":
        return point[0] - cow[1]
    else:
        return point[1] - cow[2]

n = int(input())

cows = []
for i in range(n):
    d,x,y = input().split()
    x,y = int(x),int(y)
    cows.append((d,x,y))

values = list([10**10]*n for _ in range(n))
for i in range(n):
    for j in range(n):
        if i != j and cows[i][0] != cows[j][0]:

            cow1 = (cows[i])
            cow2 = (cows[j])
            P = (max(cow1[1],cow2[1]),max(cow1[2],cow2[2]))

            d1 = distToPoint(cow1,P)
            d2 = distToPoint(cow2,P)

            if d1 > 0 and d2 > 0:
                if d1 > d2:
                   values[i][j] = d1
                elif d2 > d1:
                    values[j][i] = d2

minim = []
for i in range(n):
    minim.append((i,min(values[i])))

for i in range(n):
    for j in range(i+1,n):
        if minim[i][1] > minim[j][1]:
            minim[i],minim[j] = minim[j],minim[i]

for e in minim:
    idx,value = e[0],e[1]
    for i in range(n):
        if values[i][idx] > value:
            values[i][idx] = 10**10

for i in range(n):
    minim[i] = min(values[i])
    if minim[i] == 10**10:
        minim[i] = "Infinity"

print(*minim,sep="\n")


