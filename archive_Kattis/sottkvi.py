n, d, t = map(int, input().split())
party = t + d
count = 0

for i in range(n):
    s = int(input())
    release = s + 14
    if release <= party:
            count += 1

print(count)