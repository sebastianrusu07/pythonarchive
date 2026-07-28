import sys

name = "measurement"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

n = int(input())

bessie = 7
elsie = 7
mildred = 7

changes = []

for i in range(n):
    when,who,how = input().split()
    when = int(when)
    how = int(how)
    changes.append((when,who,how))

changes = sorted(changes,key=lambda x:x[0])

display = ["B","E","M"]

displayChanges = 0
for y in range(n):
    name = changes[y][1]
    change = changes[y][2]
    if name == "Bessie":
        bessie += change
    elif name == "Elsie":
        elsie += change
    else:
        mildred += change

    newDisplay = []
    neededToDisplay = max(bessie,max(elsie,mildred))
    if neededToDisplay == bessie:
        newDisplay.append("B")
    if neededToDisplay == elsie:
        newDisplay.append("E")
    if neededToDisplay == mildred:
        newDisplay.append("M")

    if newDisplay != display:
        display = newDisplay
        displayChanges += 1

print(displayChanges)