import sys

name = "cownomics"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

n,m = map(int,input().split())

spotty = []
for i in range(n):
    row = input()
    spotty.append(row)

plain = []
for i in range(n):
    row = input()
    plain.append(row)

uniques = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
                spottyTuples = set()
                for l in range(n):
                    spottyTuples.add((spotty[l][i], spotty[l][j], spotty[l][k]))

                ok = True
                for l in range(n):
                    if (plain[l][i], plain[l][j], plain[l][k]) in spottyTuples:
                        ok = False
                        break

                if ok:
                    uniques+=1


print(uniques)