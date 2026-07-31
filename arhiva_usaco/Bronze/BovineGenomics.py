import sys
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

k,n = map(int,input().split())

spotty = [input() for _ in range(k)]
plain = [input() for _ in range(k)]

impGenes = 0
for i in range(n):
    columnSpotted = set()
    columnPlain = set()
    for j in range(k):
        columnSpotted.add(spotty[j][i])
        columnPlain.add(plain[j][i])

    if len(columnSpotted & columnPlain) == 0:
        impGenes += 1

print(impGenes)




