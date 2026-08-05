if __name__ == "__main__":
    days,startingCost = map(int,input().split())

    minCost = startingCost+1
    dayList = list(map(int,input().split()))

    for i in range(1,days):
        if dayList[i]-dayList[i-1]<=startingCost+1:
            minCost += dayList[i]-dayList[i-1]
        else:
            minCost += startingCost+1

    print(minCost)
