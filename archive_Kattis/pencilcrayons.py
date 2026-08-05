n,m = map(int,input().split())

cnt = 0
for i in range(n):
    line = set(input().split())
    cnt += m - len(line)

print(cnt)