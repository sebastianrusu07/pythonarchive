line = input().split()

row,column = line[0],line[1]

grid = []
for i in range(len(column)):
    rowCreate = []
    for j in range(len(row)):
        rowCreate.append('.')
    grid.append(rowCreate)

for i in range(len(row)):
    if row[i] in column:
        posX = column.index(row[i])
        posY = i

        for j in range(len(row)):
            grid[posX][j] = row[j]

        for j in range(len(column)):
            grid[j][posY] = column[j]

        break

for i in range(len(column)):
    for j in range(len(row)):
        print(grid[i][j],end="")
    print()