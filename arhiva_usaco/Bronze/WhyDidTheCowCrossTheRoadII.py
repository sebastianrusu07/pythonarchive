import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

cowPaths = input()
cowMovements = {}
for i in range(len(cowPaths)):
    if cowPaths[i] not in cowMovements:
        cowMovements[cowPaths[i]] = [i,i]
    else:
        cowMovements[cowPaths[i]][1] = i

cows = list(cowMovements.keys())
cnt = 0
for i in range(len(cows)):
    for j in range(i):
        left1,right1 = cowMovements[cows[i]]
        left2,right2 = cowMovements[cows[j]]
        if left1 < left2 < right1 < right2 or left2 < left1 < right2 < right1:
            cnt += 1

print(cnt)










