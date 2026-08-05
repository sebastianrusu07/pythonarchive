def inRectangle(pointX,pointY,bottomLeftX,bottomLeftY,topRightX,topRightY):
    if bottomLeftX <= pointX <= topRightX and bottomLeftY <= pointY <= topRightY:
        return True

    return False

def inCircle(pointX,pointY,circleX,circleY,radius):
    dist = (pointX - circleX) ** 2 + (pointY - circleY) ** 2
    if dist <= radius ** 2 :
        return True

    return False

shapeCnt = int(input())
shapeList = []

for i in range(shapeCnt):
    line = input().split()
    shapeList.append(line)

shotCnt = int(input())
for i in range(shotCnt):
    x,y = input().split()
    x=int(x)
    y=int(y)

    shapeHit=0

    for j in range(shapeCnt):
        if shapeList[j][0]=="rectangle" and inRectangle(x,y,*map(int,shapeList[j][1:])): #very interesting!
            shapeHit+=1
        elif shapeList[j][0]=="circle" and inCircle(x,y,*map(int,shapeList[j][1:])):
            shapeHit+=1

    print(shapeHit)
