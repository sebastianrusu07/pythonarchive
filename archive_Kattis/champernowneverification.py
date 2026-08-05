n = input()

construct = ""
next = 1
while len(construct)<len(n):
    construct += str(next)
    next += 1

print (next-1 if construct==n else -1)


