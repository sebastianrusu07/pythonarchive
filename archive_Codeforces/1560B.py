peopleNrCopy = 0
def meetCriteria(a):
    return True if (peopleNrCopy >= a >= 1) else False

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a,b,c = map(int,input().split())
        diff = abs(a-b)
        peopleNr = diff*2
        peopleNrCopy = peopleNr
        dLower = c-diff
        dUpper = c+diff
        if meetCriteria(a) and meetCriteria(b) and meetCriteria(c):
            if meetCriteria(dLower):
                print(dLower)
            elif meetCriteria(dUpper):
                print(dUpper)
            else:
                print(-1)
        else:
            print(-1)
