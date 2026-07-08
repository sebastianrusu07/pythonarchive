dicti = {}

def transform(c):
    if c in dicti:
        return dicti[c]

    return c

defs,gens = map(int,input().split())

for i in range(defs):
    definition = input().split()
    dicti[definition[0]] = definition[2]

s=input()

for i in range(gens):
    sl = list(map(transform, s))
    s = "".join(sl)

print(s)