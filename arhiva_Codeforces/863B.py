if __name__ == "__main__":
    n = 2*int(input())
    weights = list(map(int, input().split()))
    weights = sorted(weights)

    stablestOutcome = float("inf")
    for one in range(n):
        for two in range(one+1,n):
            doubleKayaks = weights[:]
            del doubleKayaks[two]
            del doubleKayaks[one]
            instability = 0
            for i in range(0,n-2,2):
                instability += doubleKayaks[i+1]-doubleKayaks[i]
            stablestOutcome = min(stablestOutcome, instability)
    print(stablestOutcome)






