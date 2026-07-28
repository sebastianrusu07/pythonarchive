import sys

name = "censor"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

text = list(input().strip())
target = list(input().strip())
targetLen = len(target)

stack = []
for i in range(len(text)):
    stack.append(text[i])
    if stack[-targetLen:] == target:
        del stack[-targetLen:]

print(*stack,sep="")


