def relativeToSide(l1x,l1y,l2x,l2y,px,py):
    formula = ( l2x - l1x ) * ( py - l1y ) - ( l2y - l1y ) * ( px - l1x )
    return formula


ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
area = abs(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))/2

points = int(input())
cnt = 0
for i in range(points):
    px,py = map(int,input().split())

    res1 = relativeToSide(ax,ay,bx,by,px,py)
    res2 = relativeToSide(bx,by,cx,cy,px,py)
    res3 = relativeToSide(cx,cy,ax,ay,px,py)

    neg = 0
    pos = 0

    if res1 > 0:
        pos += 1
    elif res1 < 0:
        neg += 1

    if res2 > 0:
        pos += 1
    elif res2 < 0:
        neg += 1

    if res3 > 0:
        pos += 1
    elif res3 < 0:
        neg += 1

    if (neg != 0 and pos == 0 ) or ( neg == 0 and pos != 0):
        cnt += 1

print(area,cnt,sep='\n')