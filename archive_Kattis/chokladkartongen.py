n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(1,n):
    if numbers[i-1] < numbers[i]:
        cnt += 1

print(cnt)