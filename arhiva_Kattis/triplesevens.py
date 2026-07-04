n = int(input())

good = True
for i in range(3):
    inputList = input().split()
    for j in range(n):
        if inputList[j]=='7':
            break
        if j==n-1:
            good = False

print ("777" if good else "0")

