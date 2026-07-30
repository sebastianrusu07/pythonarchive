import sys

name = "balancing"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

cows,n = map(int,input().split())

cowList = []
for i in range(cows):
    cowList.append(tuple(map(int,input().split())))

smallestTotal = float("inf")
for _,Y in cowList:
    for X,_ in cowList:
        x = X+1
        y = Y+1
        NE,SE,SW,NW = 0,0,0,0
        for cow in cowList:
            if cow[0] < x:
                if cow[1] < y:
                    SW+=1
                else:
                    NW+=1
            else:
                if cow[1] < y:
                    SE+=1
                else:
                    NE+=1
        smallestTotal = min(smallestTotal,max(NE,NW,SE,SW))

print(smallestTotal)