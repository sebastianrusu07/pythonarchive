import sys

data = list(map(int, sys.stdin.read().split()))

pos = 0

n = data[pos]
pos += 1

nList = set(data[pos:pos+n])
pos += n

m = data[pos]
pos += 1

mList = set(data[pos:pos+m])

print(*sorted(mList | nList))
print(*sorted(mList & nList))