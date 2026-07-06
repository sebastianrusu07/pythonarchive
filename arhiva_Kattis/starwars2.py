n = int(input())

numbers = input().split()
numbers.sort(key=int)
size = int(len(numbers))
print(*numbers[size//3:size//3*2],*numbers[:size//3],*numbers[size//3*2:],sep=" ")