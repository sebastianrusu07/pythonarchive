grid = []
n,u = map(int, input().split())

for i in range(n):
    row = list(input().strip())
    grid.append(row)

kGroups = []

def changesToReflection():
    length = n//2
    total = 0
    for i in range(length):
        row = []
        for j in range(length):
            tr = (i,length + j)
            tl = (i,length - j -1)
            br = (n - i - 1, length + j)
            bl = (n - i - 1, length - j - 1)

            k = (grid[tr[0]][tr[1]] == '#') + (grid[tl[0]][tl[1]] == '#') + (grid[br[0]][br[1]] == '#') + (grid[bl[0]][bl[1]] == '#')
            toChange = min(k,4-k) #either change them to be . or to be #
            total+=toChange
            row.append(k)
        kGroups.append(row)

    return total

total = changesToReflection()

print(total)
for i in range(u):
    x,y = map(int,input().split())
    y-=1
    x-=1

    X = x if x<n//2 else n-x-1
    Y = n//2-y-1 if y<n//2 else y - n//2

    k = kGroups[X][Y]
    total-=min(k,4-k)
    if grid[x][y] == '#':
        grid[x][y] = '.'
        k-=1
    else:
        grid[x][y] = '#'
        k+=1
    total+=min(k,4-k)
    kGroups[X][Y]=k
    print(total)



