import sys

name = "notlast"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

entries = int(input())

milk = {
    "Bessie":0,
    "Elsie":0,
    "Daisy":0,
    "Gertie":0,
    "Annabelle":0,
    "Maggie":0,
    "Henrietta":0
}

for i in range(entries):
    name, produced = input().split()
    produced = int(produced)

    milk[name] += produced

minimumMilk = -1
for cow in milk.values():
    if minimumMilk == -1 or cow < minimumMilk:
        minimumMilk = cow

toDelete = []
for name in milk.keys():
    if milk[name] == minimumMilk:
        toDelete.append(name)

for name in toDelete:
    del milk[name]

if len(milk) == 0:
    print("Tie")
    sys.exit(0)

minimumMilk = -1
for cow in milk.values():
    if minimumMilk == -1 or cow < minimumMilk:
        minimumMilk = cow

cows = []
for cow in milk.keys():
    if milk[cow] == minimumMilk:
        cows.append(cow)

print(cows[0] if len(cows) == 1 else "Tie")





