import sys

name = "diamond"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")


n,k = map(int,input().split())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()

i = 0
maxLen = 0
for j in range(n):
    while numbers[j] - numbers[i] > k:
        i+=1
    maxLen = max(maxLen,j-i+1)

print(maxLen)
