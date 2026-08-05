n = int(input())

inputParts = input().split()
numbers = []
for i in range(n):
    numbers.append(int(inputParts[i]))


print(sum(numbers))