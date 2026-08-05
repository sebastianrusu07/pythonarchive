import sys

minSum, n = map(int, input().split())
lockers = input()

lockers = "0" + lockers
partialSum = [0]

for i in range(1,len(lockers)):
    partialSum.append(partialSum[i-1]+int(lockers[i]))

if partialSum[-1] < minSum:
    print("impossible")
    sys.exit(0)

st=1
dr=1
smallLen=n
while dr<n:
    while dr < n and partialSum[dr]-partialSum[st-1]<minSum:
        dr+=1
    while st <= dr and partialSum[dr]-partialSum[st-1]>=minSum:
        smallLen=min(smallLen, dr-st)
        st+=1

print(smallLen)


