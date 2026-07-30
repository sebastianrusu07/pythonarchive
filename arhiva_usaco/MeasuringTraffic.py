import sys

name = "traffic"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

n = int(input())

segments = []
for i in range(n):
    type,mini,maxi = input().split()
    mini = int(mini)
    maxi = int(maxi)
    segments.append([type,mini,maxi])

lo,hi = 0,10**9
for t,a,b in segments:
    if t == "on":
        lo,hi = lo + a,hi + b
    elif t == "off":
        lo,hi = lo - b,hi - a
        if lo < 0: lo = 0
    else:
        lo,hi = max(lo, a),min(hi, b)

after = (lo,hi)

lo,hi = 0,10**9
for t,a,b in reversed(segments):
    if t == "on":
        lo,hi = lo - b,hi - a
        if lo < 0: lo = 0
    elif t == "off":
        lo,hi = lo + a,hi + b
    else:
        lo,hi = max(lo, a),min(hi, b)

before = (lo,hi)

print(*before)
print(*after)
