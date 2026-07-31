import sys

name = "mowing"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

moves = int(input())

time = 2
x = float("inf")
pos = [1000,1000]
lawn = { (1000,1000):1}

for i in range(moves):
    dire,dist = input().split()
    dist = int(dist)

    if dire == "N" :
        for i in range(dist):
            pos[1]+=1
            if tuple(pos) in lawn.keys() :
                x = min(x,abs(lawn[tuple(pos)]-time))
            lawn[tuple(pos)]=time
            time+=1
    elif dire == "S" :
        for i in range(dist):
            pos[1]-=1
            if tuple(pos) in lawn.keys() :
                x = min(x,abs(lawn[tuple(pos)]-time))
            lawn[tuple(pos)]=time
            time+=1
    elif dire == "E" :
        for i in range(dist):
            pos[0]+=1
            if tuple(pos) in lawn.keys() :
                x = min(x,abs(lawn[tuple(pos)]-time))
            lawn[tuple(pos)]=time
            time+=1
    else:
        for i in range(dist):
            pos[0]-=1
            if tuple(pos) in lawn.keys() :
                x = min(x,abs(lawn[tuple(pos)]-time))
            lawn[tuple(pos)]=time
            time+=1

print(-1 if x == float("inf") else x)

