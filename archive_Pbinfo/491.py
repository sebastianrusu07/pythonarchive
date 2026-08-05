n = int(input())

inputParts = input().split()
numbers = []

firstEven = -1
lastEven = -1

for i in range(n):
    numbers.append(int(inputParts[i]))
    if numbers[i] % 2 == 0:

        if firstEven == -1:
            firstEven = i

        lastEven = i

if firstEven != -1:
    print(sum(numbers[firstEven:lastEven+1]))
else:
    print("NU EXISTA")