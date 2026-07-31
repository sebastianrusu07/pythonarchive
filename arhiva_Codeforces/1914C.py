t = int(input())

for case in range(t):
    n,k = map(int,input().split())
    first = list(map(int,input().split()))
    after = list(map(int,input().split()))

    optimalExpGain = 0
    toUnlock = 0
    maxSubsequent = 0
    for questsUnlocked in range(1,min(k,n)+1):
        toUnlock += first[questsUnlocked-1]
        maxSubsequent = max(maxSubsequent,after[questsUnlocked-1])
        projectedExpGain = maxSubsequent *(k-questsUnlocked) + toUnlock
        optimalExpGain = max(optimalExpGain, projectedExpGain)

    print(optimalExpGain)






