t = int(input())

for case in range(t):
    n,B,H = map(int,input().split())
    positions = list(map(int,input().split()))

    avgArea = B * H / 2
    totalArea = avgArea
    for i in range(n-1):
        if positions[i] + H <= positions[i+1]:
            totalArea += avgArea
        else:
            hM = positions[i+1] - positions[i]
            hm = H - hM
            x = H/hm
            b = B/x
            smallArea = hm * b /2

            totalArea += avgArea - smallArea
    print(f"{totalArea:.7f}")

