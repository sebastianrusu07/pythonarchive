minX=99999999999
maxX=-9999999999
minY=99999999999
maxY=-99999999999

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    minX = min(minX,x)
    maxX = max(maxX,x)
    minY = min(minY,y)
    maxY = max(maxY,y)

print((maxX-minX+2)*2 + (maxY-minY+2)*2)