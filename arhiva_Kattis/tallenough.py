n = int(input())

good = True

for i in range(n):
    height = int(input())
    if height<48:
        good = False

print(good)