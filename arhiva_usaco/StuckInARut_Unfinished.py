n = int(input())

cows = []
for i in range(n):
    d,x,y = input().split()
    x,y = int(x),int(y)
    cows.append((d,x,y))

values = list([0]*n for _ in range(n))
for i in range(n):
    for j in range(n):
        if i != j and cows[i][0] != cows[j][0]:
            N,E = 0,0
            if cows[i][0] == "N":
                N = (cows[i][1],cows[i][2])
                E = (cows[j][1],cows[j][2])
            else:
                N = (cows[j][1],cows[j][2])
                E = (cows[i][1],cows[i][2])

            if E[0] < N[0] and E[1] > N[1]:
                a = N[0] - E[0]
                b = E[1] - N[1]
                if a < b and values[j][i] == 0 and values[i][j] != -1:
                    values[i][j] = 1
                    values[j][i] = -1
                elif a > b and values[i][j] == 0 and values[j][i] != -1:
                    values[i][j] = -1
                    values[j][i] = 1
            print(values)



for i in range(n):
    firstMeet = float("inf")
    for j in range(n):
        if values[i][j] == -1:
            if cows[i][0] == "N":
                firstMeet = min(firstMeet,cows[j][2]-cows[i][2])
            else:
                firstMeet = min(firstMeet,cows[j][1]-cows[i][1])
    print(firstMeet if firstMeet != float("inf") else "Infinity")

