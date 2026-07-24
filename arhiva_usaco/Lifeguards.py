import sys

name = "lifeguards"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")



lifeguards = int(input())

hours = [0]*1001
lifeguardList = []

for i in range(lifeguards):
    start,end = map(int,input().split())
    for i in range(start,end):
        hours[i] += 1
    lifeguardList.append([start,end])

minShiftsLost = -1
for guy in lifeguardList:
    start,end = guy[0],guy[1]
    shiftsLost = 0
    for i in range(start,end):
        if hours[i] <= 1:
            shiftsLost += 1

    if minShiftsLost == -1 or shiftsLost < minShiftsLost:
        minShiftsLost = shiftsLost

totalHours = 0
for i in range(1000):
    if hours[i] >= 1:
        totalHours += 1

print(totalHours-minShiftsLost)

