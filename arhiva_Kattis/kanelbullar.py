needed = []
for i in range (5):
    needed.append(int(input()))

has = []
for i in range (5):
    has.append(int(input()))

maxBuns = has[0]//needed[0]
for j in range (1,5):
    maxBuns = min(maxBuns,has[j]//needed[j])

print(maxBuns)