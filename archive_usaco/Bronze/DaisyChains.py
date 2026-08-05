n = int(input())
flowers =  list(map(int,input().split()))

def averagePetal(i,j):
    petals = sum(flowers[i:j+1])
    avg = petals/(j-i+1)
    return avg

def hasAverageFlower(i,j):
    avg = averagePetal(i,j)
    area = flowers[i:j+1]
    return True if avg in area else False


cnt = 0
for i in range(n):
    for j in range(i,n):
        if hasAverageFlower(i,j):
            cnt += 1

print(cnt)