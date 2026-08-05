board=[]

for i in range(8):
    row=input()
    board.append(row)

availability=[]
for i in range(8):
    row = []
    for j in range(8):
        row.append(1)
    availability.append(row)


for i in range(8):
    for j in range(8):

        if board[i][j]=="R":
            for k in range(8):
                availability[i][k]=0
                availability[k][j]=0

freeSquares = 0
for i in range(8):
    freeSquares += sum(availability[i])

print(freeSquares)