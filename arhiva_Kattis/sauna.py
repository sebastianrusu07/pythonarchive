people = int(input())

totalLeast=-1
totalMost=-1
for i in range(people):
    line = input().split()
    least,most = int(line[0]),int(line[1])

    if totalLeast == -1 or least > totalLeast :
        totalLeast = least

    if totalMost == -1 or most < totalMost :
        totalMost = most

if totalLeast > totalMost:
    print("bad news")
else:
    print(totalMost - totalLeast + 1,totalLeast,sep=" ")