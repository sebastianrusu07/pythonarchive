import sys

n, k = map(int, input().split())

numbers = list(map(int, input().split()))
sortedNumbers = sorted(numbers)

st=0
dr=n-1

while st<dr:
    sum=sortedNumbers[st]+sortedNumbers[dr]
    if sum>k:
        dr-=1
    elif sum<k:
        st+=1
    else:
        a=numbers.index(sortedNumbers[st])
        b=n-numbers[::-1].index(sortedNumbers[dr])-1
        if a>b:
            a,b=b,a
        print(a+1,b+1,sep=" ")
        sys.exit(0)

print("IMPOSSIBLE")