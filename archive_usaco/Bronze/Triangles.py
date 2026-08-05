import sys

name = "triangles"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")

n = int(input())

coords = []
for i in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))

maxArea = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i!=k:
                ix,iy = coords[i][0],coords[i][1]
                jx,jy = coords[j][0],coords[j][1]
                kx,ky = coords[k][0],coords[k][1]

                if ix == jx and iy == ky:
                    area = abs(jy - iy) * abs(kx - ix)
                    maxArea = max(maxArea, area)

print(maxArea)

