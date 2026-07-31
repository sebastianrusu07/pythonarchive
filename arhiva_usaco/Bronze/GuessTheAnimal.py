import sys

name = "guess"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

def commonCharCnt(a,b):
    set1 = set(a)
    set2 = set(b)
    return len(set1.intersection(set2))


n = int(input())

chars = []
for i in range(n):
    line = input().split()
    chars.append(line[2:])

maxIntersect = 0
for i in range(n):
    for j in range(n):
        if i != j:
            maxIntersect = max(maxIntersect,commonCharCnt(chars[i],chars[j]))

print(maxIntersect+1)