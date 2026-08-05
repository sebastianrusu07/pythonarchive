a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

maxDif = max(b-a,c-b)
maxHops = maxDif - 1

print(maxHops)

