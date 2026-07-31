n = int(input())

cows = []
for _ in range(n):
    direction, p = input().split()
    cows.append((direction, int(p)))

best = n

for direction, x in cows:
    liars = 0

    for d, p in cows:
        if d == "L" and x > p:
            liars += 1
        elif d == "G" and x < p:
            liars += 1

    if liars < best:
        best = liars

print(best)