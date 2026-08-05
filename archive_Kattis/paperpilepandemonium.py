line1 = input().split()
nrPapers, stacks = int(line1[0]),int(line1[1])

grid = []
for i in range(stacks):
    line2 = input().split()
    grid.append(line2[1:])

movements = int(input())
for i in range(movements):
    line3 = input().split()
    source, dest, cnt=int(line3[0])-1,int(line3[1])-1,int(line3[2])
    grid[dest].extend(grid[source][-cnt:])
    del grid[source][-cnt:]

for i in range(stacks):
    print(*grid[i])