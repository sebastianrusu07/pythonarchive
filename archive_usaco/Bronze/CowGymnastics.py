import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

k,n = map(int,input().split())

arr = list(list(0 for y in range(n+1)) for i in range(k+1))
for i in range(1,k+1):
    line = list(map(int,input().split()))
    for j in range(n):
        arr[i][line[j]] = j+1

cnt = 0
for i in range(1,n+1):
    for j in range(1,i):
        bal = 0
        for y in range(1,k+1):
            if arr[y][i] > arr[y][j]:
                bal += 1
            else :
                bal -= 1

        if abs(bal) == k:
            cnt += 1

print(cnt)